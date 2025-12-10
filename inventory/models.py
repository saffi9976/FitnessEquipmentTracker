from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('Cardio', 'Cardio'),
        ('Strength', 'Strength'),
        ('Accessory', 'Accessory'),
    ]

    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=EQUIPMENT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    # Relationship to Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # -------------------------------
    #   VALIDATION (REQUIRED)
    # -------------------------------
    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

        if self.stock < 0:
            raise ValidationError("Stock cannot be negative.")

        if not self.name.strip():
            raise ValidationError("Name cannot be empty.")

        if not self.manufacturer.strip():
            raise ValidationError("Manufacturer cannot be empty.")

    def __str__(self):
        return f"{self.name} ({self.type})"

    # -------------------------------
    #   DATABASE INDEXES (REQUIRED)
    # -------------------------------
    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['manufacturer']),
            models.Index(fields=['category']),
            models.Index(fields=['type']),
        ]


class MaintenanceRecord(models.Model):
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='maintenance_records'
    )
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.equipment.name} – {self.date}"
