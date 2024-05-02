# populate_menu_items.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OBSystem.settings")
django.setup()

from system.models import MenuCategory, MenuItem

def populate_items():
    categories = ['Tiffins', 'Main Course', 'Fast Foods', 'Beverages', 'Desserts']
    
    tiffins = [
        ('Idli', 2.50),
        ('Dosa', 3.00),
        ('Upma', 2.75),
        ('Pongal', 3.25),
        ('Vada', 2.00),
        ('Puri', 2.50),
        ('Uttapam', 3.50),
        ('Kesari', 3.00),
        ('Rava Dosa', 3.50),
        ('Appam', 3.25),
        ('Masala Dosa', 4.00),
        ('Set Dosa', 3.75),
        ('Poori Bhaji', 4.50),
        ('Rava Upma', 3.00),
        ('Rava Idli', 3.25),
        ('Medu Vada', 2.25),
        ('Pesarattu', 3.00),
        ('Onion Dosa', 3.50),
        ('Masala Uttapam', 4.00),
        ('Plain Dosa', 3.00),
    ]

    main_course = [
        ('Roti', 1.50),
        ('Naan', 2.00),
        ('Butter Naan', 2.50),
        ('Garlic Naan', 3.00),
        ('Chapati', 1.00),
        ('Paratha', 2.50),
        ('Vegetable Biryani', 8.00),
        ('Chicken Biryani', 9.50),
        ('Mutton Biryani', 10.50),
        ('Paneer Butter Masala', 7.50),
        ('Chicken Curry', 8.50),
        ('Mutton Curry', 9.50),
        ('Fish Curry', 10.00),
        ('Veg Fried Rice', 7.00),
        ('Egg Fried Rice', 7.50),
        ('Chicken Fried Rice', 8.50),
        ('Veg Pulao', 7.00),
        ('Egg Curry', 8.00),
        ('Dal Tadka', 6.00),
        ('Shahi Paneer', 8.00),
    ]

    beverages = [
        ('Tea', 1.50),
        ('Coffee', 2.00),
        ('Espresso', 2.50),
        ('Cappuccino', 3.00),
        ('Latte', 3.50),
        ('Hot Chocolate', 3.50),
        ('Milkshake', 4.00),
        ('Orange Juice', 2.50),
        ('Apple Juice', 2.50),
        ('Pineapple Juice', 2.50),
        ('Lemonade', 2.00),
        ('Iced Tea', 2.50),
        ('Iced Coffee', 3.00),
        ('Soda', 1.50),
        ('Mineral Water', 1.00),
        ('Buttermilk', 1.50),
        ('Lassi', 2.50),
    ]

    fast_foods = [
        ('Burger', 4.50),
        ('Cheeseburger', 5.00),
        ('Chicken Burger', 5.50),
        ('Veggie Burger', 4.50),
        ('Pizza', 10.00),
        ('French Fries', 3.00),
        ('Onion Rings', 3.50),
        ('Hot Dog', 4.00),
        ('Sandwich', 5.00),
        ('Wrap', 5.50),
        ('Tacos', 4.50),
        ('Quesadillas', 6.00),
        ('Nachos', 6.00),
        ('Chicken Wings', 7.50),
        ('Spring Rolls', 4.00),
        ('Samosas', 3.50),
        ('Pakoras', 3.00),
        ('Fried Chicken', 7.00),
        ('Popcorn Shrimp', 8.00),
    ]

    desserts = [
        ('Ice Cream', 3.99),
        ('Sundae', 4.99),
        ('Cake', 4.50),
        ('Pie', 3.75),
        ('Brownie', 2.99),
        ('Cookies', 1.99),
        ('Cupcake', 2.50),
        ('Pudding', 3.25),
        ('Donuts', 1.50),
        ('Tart', 4.25),
        ('Pastry', 2.75),
        ('Mousse', 4.50),
        ('Trifle', 4.75),
        ('Parfait', 3.99),
        ('Gelato', 4.25),
        ('Sorbet', 3.50),
        ('Cheesecake', 5.25),
        ('Tiramisu', 5.50),
        ('Baklava', 3.99),
    ]

    categories_items = {
        'Tiffins': tiffins,
        'Main Course': main_course,
        'Beverages': beverages,
        'Fast Foods': fast_foods,
        'Desserts': desserts
    }

    for category_name in categories:
        category, created = MenuCategory.objects.get_or_create(name=category_name)
        items = categories_items.get(category_name, [])
        for item in items:
            MenuItem.objects.get_or_create(category=category, name=item[0], price=item[1])

if __name__ == '__main__':
    print("Populating Menu Items...")
    populate_items()
    print("Menu Items populated successfully!")
