from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/', views.add_equipment, name='add_equipment'),
    path('update/<int:pk>/', views.update_equipment, name='update_equipment'),
    path('delete/<int:pk>/', views.delete_equipment, name='delete_equipment'),

    # CATEGORY CRUD
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/update/<int:pk>/', views.update_category, name='update_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),

    # Maintenance CRUD
    path('maintenance/', views.maintenance_list, name='maintenance_list'),
    path('maintenance/add/', views.add_maintenance, name='add_maintenance'),
    path('maintenance/update/<int:pk>/', views.update_maintenance, name='update_maintenance'),
    path('maintenance/delete/<int:pk>/', views.delete_maintenance, name='delete_maintenance'),

    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/json/', views.export_json, name='export_json'),
    path('export/txt/', views.export_txt, name='export_txt'),

    # Import
    path('import/', views.import_csv, name='import_csv'),
]
