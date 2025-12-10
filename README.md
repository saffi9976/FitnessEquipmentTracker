# Fitness Equipment Tracker

A web-based system to manage fitness equipment, categories, and maintenance records.  
The app allows users to:

- Add, update, delete, and search equipment.
- Manage categories of equipment.
- Track maintenance records for each equipment item.
- Import/export inventory data in CSV, JSON, and TXT formats.
- Receive low-stock alerts via signals.

## Key Features:
- CRUD operations for Equipment, Category, and MaintenanceRecord.
- Search and pagination for large inventories.
- File import/export for data persistence and backup.
- Security via Django forms, CSRF protection, and ORM queries.


1. Class Diagram:
<img width="2064" height="672" alt="image" src="https://github.com/user-attachments/assets/ea76e476-3942-42e3-acce-f7cf51ca32dc" />


Sequence Diagram:
User -> Template/Form: Submit EquipmentForm(name, manufacturer, type, price, stock, category)
Template -> View: POST /inventory/add/
View -> Form: Validate input
Form -> Model/ORM: Equipment.objects.create()
Model/ORM -> DB: INSERT INTO inventory_equipment (...)
DB -> Model/ORM: OK
Model/ORM -> View: Equipment instance
View -> Signal: Trigger low_stock_alert if stock < 3
Signal -> View: Alert processed
View -> Template: Render inventory_list.html with success message
Template -> User: Updated equipment list

