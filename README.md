## CREATE A `.env` FILE IN ROOT AND ENTER THIS:

SECRET_KEY='your_secret_key_here'
DEBUG=True
DB_NAME=fitness_db
DB_USER=root
DB_PASSWORD=password
DB_HOST=127.0.0.1
DB_PORT=3306


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


