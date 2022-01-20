from django.test import TestCase

from inventory.models import Item


class ItemListViewTest(TestCase):
    """
    Test case for list view of inventory
    """
    @classmethod
    def setUpTestData(cls):
        # Create 13 items for pagination tests
        number_of_items = 13

        for item_id in range(number_of_items):
            Item.objects.create(
                sku=f"item-{item_id}",
                title=f"title{item_id}",
                count=100,
                active=True)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)


    def test_view_uses_correct_template(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/inventory_table.html')

    def test_pagination_is_ten(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['inventory']), 10)

    def test_lists_all_items(self):
        # second page should only have 3 items
        response = self.client.get('/inventory/' + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['inventory']), 3)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)

