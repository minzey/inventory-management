# inventory-management

Inventory management application lets users perform CRUD operations on inventory items, and download an export of inventory in a CSV file.

Extra feature attempted - **Export inventory to CSV**

## Stack used
**Framework (Backend + Templating):** Django

**Database:** SQLite3

**Frontend:** Bootstrap


## How to run the application

1. Clone the application code
2. `cd` into the cloned repository
3. Install python3. The application has been tested on python3.8
5. Create a new virtual env to install dependencies with appropriate versions : `python3 -m venv env` - here env is the name of your virtual env
6. Activate virtual env: `source env/bin/activate`
7. Install dependencies: `python -m pip install -r requirements.txt`
8. Run migrations to change database schema: `python manage.py migrate`
9. Run application: `python manage.py runserver`
10. Access the app at `http://127.0.0.1:8000/`
