from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Item(models.Model):
    """
    An item in the inventory
    """
    sku = models.SlugField(max_length=50, primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=250, db_index=True)
    description = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True, help_text="comma separated list of tags")
    count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(default=timezone.now)
    last_modified_at = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    active = models.BooleanField(default=False, help_text="an active item is visible in shop")

    def __str__(self):
        return f"{self.sku}: {self.title}"

    class Meta:
        ordering = ['-active', '-last_modified_at']





