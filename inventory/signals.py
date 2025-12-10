from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Equipment

@receiver(post_save, sender=Equipment)
def low_stock_alert(sender, instance, **kwargs):
    try:
        stock_value = int(instance.stock)
    except:
        return  # skip if not a number (during CSV import)

    if stock_value < 3:
        print(f"LOW STOCK WARNING: {instance.name} only has {stock_value} left!")
