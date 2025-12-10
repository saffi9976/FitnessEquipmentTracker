from django import forms
from .models import Equipment, Category, MaintenanceRecord

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'manufacturer', 'type', 'price', 'stock', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['equipment', 'date', 'description']


from django import forms
from .models import Equipment, Category, MaintenanceRecord

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'manufacturer', 'type', 'price', 'stock', 'category']

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        return price


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['equipment', 'date', 'description']
