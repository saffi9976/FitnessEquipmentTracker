from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
import csv
import json

from .models import Equipment, Category, MaintenanceRecord
from .forms import EquipmentForm, CategoryForm, MaintenanceRecordForm

def inventory_list(request):
    items = Equipment.objects.all().order_by('id')
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            name__icontains=search_query
        ) | items.filter(
            category__name__icontains=search_query
        ) | items.filter(
            manufacturer__icontains=search_query
        ) | items.filter(
            type__icontains=search_query
        )
    paginator = Paginator(items, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'inventory/inventory_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipment added successfully!")
            return redirect('inventory_list')
    else:
        form = EquipmentForm()
    return render(request, 'inventory/add_equipment.html', {'form': form})

def update_equipment(request, pk):
    item = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipment updated successfully!")
            return redirect('inventory_list')
    else:
        form = EquipmentForm(instance=item)
    return render(request, 'inventory/update_equipment.html', {'form': form, 'item': item})

def delete_equipment(request, pk):
    item = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.warning(request, "Equipment deleted.")
        return redirect('inventory_list')
    return render(request, 'inventory/delete_equipment.html', {'item': item})

def category_list(request):
    categories = Category.objects.all().order_by('id')
    search_query = request.GET.get('search', '')
    if search_query:
        categories = categories.filter(name__icontains=search_query)
    paginator = Paginator(categories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'inventory/category_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'inventory/add_category.html', {'form': form})

def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'inventory/update_category.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.warning(request, "Category deleted.")
        return redirect('category_list')
    return render(request, 'inventory/delete_category.html', {'category': category})

def maintenance_list(request):
    records = MaintenanceRecord.objects.all().order_by('-date')
    search_query = request.GET.get('search', '')
    if search_query:
        records = records.filter(
            equipment__name__icontains=search_query
        ) | records.filter(
            description__icontains=search_query
        )
    paginator = Paginator(records, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'inventory/maintenance_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

def add_maintenance(request):
    if request.method == 'POST':
        form = MaintenanceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Maintenance record added!")
            return redirect('maintenance_list')
    else:
        form = MaintenanceRecordForm()
    return render(request, 'inventory/add_maintenance.html', {'form': form})

def update_maintenance(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == 'POST':
        form = MaintenanceRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Maintenance record updated!")
            return redirect('maintenance_list')
    else:
        form = MaintenanceRecordForm(instance=record)
    return render(request, 'inventory/update_maintenance.html', {'form': form})

def delete_maintenance(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.warning(request, "Maintenance record deleted.")
        return redirect('maintenance_list')
    return render(request, 'inventory/delete_maintenance.html', {'record': record})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="equipment_export.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Manufacturer', 'Type', 'Price', 'Stock', 'Category'])
    for item in Equipment.objects.all():
        writer.writerow([
            item.name,
            item.manufacturer,
            item.type,
            item.price,
            item.stock,
            item.category.name if item.category else ""
        ])
    messages.success(request, "CSV exported successfully!")
    return response

def export_json(request):
    data = []
    for item in Equipment.objects.all():
        data.append({
            'name': item.name,
            'manufacturer': item.manufacturer,
            'type': item.type,
            'price': float(item.price),
            'stock': item.stock,
            'category': item.category.name if item.category else "",
        })
    response = HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="equipment_export.json"'
    messages.success(request, "JSON exported successfully!")
    return response

def export_txt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="equipment_export.txt"'
    for item in Equipment.objects.all():
        line = (
            f"Name: {item.name} | Manufacturer: {item.manufacturer} | "
            f"Type: {item.type} | Price: {item.price} | "
            f"Stock: {item.stock} | Category: {item.category.name if item.category else ''}\n"
        )
        response.write(line)
    messages.success(request, "TXT exported successfully!")
    return response

def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file')
        if not csv_file or not csv_file.name.endswith('.csv'):
            messages.error(request, "Invalid file — upload a .csv file.")
            return redirect('import_csv')
        file_data = csv_file.read().decode("utf-8").splitlines()
        reader = csv.reader(file_data)
        next(reader)
        for row in reader:
            name, manufacturer, type, price, stock, category_name = row
            category_obj, created = Category.objects.get_or_create(name=category_name)
            Equipment.objects.create(
                name=name,
                manufacturer=manufacturer,
                type=type,
                price=price,
                stock=stock,
                category=category_obj
            )
        messages.success(request, "CSV imported and data added successfully!")
        return redirect('inventory_list')
    return render(request, 'inventory/import_csv.html')
