⚠️db.sqlite3 should be in .gitignore, it was added for the purpose of facilitating local testing

Run Server: 
```bash 
    python manage.py runserver
````
Create module: 
```bash 
    python manage.py startapp [module_name]
````

To add more fields to an existing model in Django
Here's the detailed process:

Edit the models.py file: Add the new field to your model's class definition.

Create the migration: Open the terminal in your Django project folder and run the command:
```bash 
    python manage.py makemigrations
````

This generates a migration file that records the change made to your model, but does not apply it to the database.
Apply the migration: To apply the change to your database structure, run the command:
```bash 
    python manage.py migrate
````