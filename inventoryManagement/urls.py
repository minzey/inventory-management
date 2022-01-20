"""inventoryManagement URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from inventory.views import redirect_root


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_root, name='home'),
    path('inventory/', include('inventory.urls'))
]
