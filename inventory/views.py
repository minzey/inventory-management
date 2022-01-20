from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from inventory.export_helper import export_inventory_csv
from inventory.models import Item


def redirect_root(request):
    return HttpResponseRedirect('/inventory/')


class SetTimezoneView(View):
    """
    Sets the timezone of the application to the selected value. All common timezones are available.
    """

    def post(self, request, *args, **kwargs):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')


class ItemListView(ListView):
    """
    List View to retrieve a paginated list of all items in the inventory. Items are sorted in descending order of
    last modified time, active items are shown first.
    """
    context_object_name = 'inventory'
    template_name = 'inventory/inventory_table.html'
    paginate_by = 10
    queryset = Item.objects.all()



class ItemCreateView(SuccessMessageMixin, CreateView):
    """
    Create View for adding an item to the inventory. Validations for non negative input for item quantity (added in
    model definition), and sanitization of user input for protection against SQL injection, is handled by the
    framework.
    """
    model = Item
    fields = [
        'sku', 'active', 'title', 'description', 'metadata', 'price', 'count'
    ]
    success_message = 'Item added to inventory!'

    def get_success_url(self):
        return reverse('inventory-list')


class ItemDetailView(DetailView):
    """
    Detail View of an item returns all fields of the model Item.
    """
    model = Item


class ItemUpdateView(SuccessMessageMixin, UpdateView):
    """
    Update View of an item does not allow updation og SKU. Created_at, and Last_modified_at fields are not
    managed by the user.
    """
    model = Item
    fields = [
        'title', 'active', 'description', 'metadata', 'price', 'count'
    ]
    success_message = 'Item updated!'

    def get_success_url(self):
        return reverse('inventory-list')


class ItemDeleteView(SuccessMessageMixin, DeleteView):
    """
    Delete View that allows deletion of a single item from the inventory.
    """
    model = Item

    def get_success_url(self):
        self.success_message = f"Item {self.get_object().sku} - {self.get_object().title} was deleted!"
        return reverse('inventory-list')

class ExportToCsv(View):
    """
    View to export the entire inventory to a csv file. This works well for a million records but has not been
    developed for a scale larger than that. A streaming http response would need to be returned for huge number of
    records so that request does not time out while data is being prepared for export.
    """

    def get(self, request, *args, **kwargs):

        csv_headers = ["SKU", "Title", "Description", "Tags", "Price", "Quantity", "Date Added", "Date Last Modified", "Status"]
        model_fields = ['sku', 'title', 'description', 'metadata', 'price', 'count', 'created_at',
                        'last_modified_at', 'active']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="inventory.csv"'

        writer = export_inventory_csv(model_fields, csv_headers, response)

        return response
