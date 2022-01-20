"""inventoryManagement URL Configuration
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.ItemListView.as_view(), name='inventory-list'),
    path('add', views.ItemCreateView.as_view(), name='add-item'),
    path('export', views.ExportToCsv.as_view(), name='export-all-items-csv'),
    path('<pk>/update', views.ItemUpdateView.as_view(), name='edit-item'),
    path('<pk>/delete', views.ItemDeleteView.as_view(), name='delete-item'),
    path('<pk>', views.ItemDetailView.as_view(), name='detail-item'),
    path('timezone/', views.SetTimezoneView.as_view(), name='set-timezone'),

]
