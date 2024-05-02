# populate_menu_categories.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OBSystem.settings")
django.setup()

from system.models import MenuCategory

def populate_menu_categories():
    categories = ['Tiffins', 'Main Course', 'Fast Foods', 'Beverages','Desserts']
    for category_name in categories:
        MenuCategory.objects.get_or_create(name=category_name)

if __name__ == '__main__':
    print("Populating Menu Categories...")
    populate_menu_categories()
    print("Menu Categories populated successfully!")
