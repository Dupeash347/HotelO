
from django.shortcuts import render, redirect
from .models import MenuCategory
from .models import MenuItem
from .models import Order
from django.contrib import messages
from django.db.models import Sum
from datetime import datetime, timedelta
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np

def prehome(request):
    if request.method == 'POST':
        table_number = request.POST.get('table_number')
        request.session['table_number'] = table_number
        return redirect('homepage')  # Redirect to your home page
    else:
        return render(request, 'prehome.html')


def homepage(request):
    categories = MenuCategory.objects.all()
    return render(request, 'homepage.html', {'categories': categories})

def add_to_order(request):
    if request.method == 'POST':
        table_number = request.POST.get('table_number')
        item_id = request.POST.get('item_id')
        item = MenuItem.objects.get(pk=item_id)
        order, created = Order.objects.get_or_create(table_number=table_number, status='Open')
        order.items.add(item)
        order.save()
        return redirect('homepage')
    else:
        return redirect('homepage')
    
def orders(request):
    table_number = request.session.get('table_number')
    orders = Order.objects.filter(table_number=table_number, status='Open')
    total_price = sum([order_item.price for order in orders for order_item in order.items.all()])
    return render(request, 'orders.html', {'orders': orders, 'total_price': total_price})


def remove_from_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        item_id = request.POST.get('item_id')
        order = Order.objects.get(pk=order_id)
        item = MenuItem.objects.get(pk=item_id)
        order.items.remove(item)
        return redirect('orders')
    else:
        return redirect('orders')

def pay(request):
    table_number = request.session.get('table_number')
    orders = Order.objects.filter(table_number=table_number, status='Open')
    total_price = sum([order_item.price for order in orders for order_item in order.items.all()])
    return render(request, 'pay.html', {'orders': orders, 'total_price': total_price})

def complete_payment(request):
    if request.method == 'POST':
        table_number = request.session.get('table_number')
        orders = Order.objects.filter(table_number=table_number, status='Open')
        for order in orders:
            order.status = 'Closed'
            order.save()
        messages.success(request, 'Payment Successful!')
        return redirect('homepage')
    else:
        return redirect('homepage')
    
#stats 


# views.py



def get_revenue(start_date, end_date):
    orders = Order.objects.filter(created_at__date__range=[start_date, end_date], status='Closed')
    revenue = orders.aggregate(total_revenue=Sum('items__price'))['total_revenue'] or 0
    return revenue

def generate_graph(data, labels, title):
    plt.figure(figsize=(10, 5))
    plt.bar(labels, data, color='blue')
    plt.xlabel('Time Interval')
    plt.ylabel('Revenue')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convert the plot to a PNG image
    image = BytesIO()
    plt.savefig(image, format='png')
    plt.close()

    # Encode the PNG image to base64
    encoded_image = base64.b64encode(image.getvalue()).decode('utf-8')
    return encoded_image

def daily_revenue(request):
    today = datetime.now().date()
    revenue = get_revenue(today, today)
    labels = [today.strftime('%Y-%m-%d')]
    data = [revenue]
    graph = generate_graph(data, labels, 'Daily Revenue')
    return render(request, 'revenue.html', {'revenue': revenue, 'graph': graph})

def weekly_revenue(request):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    revenue = get_revenue(start_of_week, end_of_week)
    labels = [start_of_week.strftime('%Y-%m-%d'), end_of_week.strftime('%Y-%m-%d')]
    data = [revenue]
    graph = generate_graph(data, labels, 'Weekly Revenue')
    return render(request, 'revenue.html', {'revenue': revenue, 'graph': graph})

def monthly_revenue(request):
    today = datetime.now().date()
    start_of_month = today.replace(day=1)
    end_of_month = start_of_month.replace(day=28) + timedelta(days=4)
    revenue = get_revenue(start_of_month, end_of_month)
    labels = [start_of_month.strftime('%Y-%m-%d'), end_of_month.strftime('%Y-%m-%d')]
    data = [revenue]
    graph = generate_graph(data, labels, 'Monthly Revenue')
    return render(request, 'revenue.html', {'revenue': revenue, 'graph': graph})

# Similarly, you can create functions for quarterly, half-yearly, and yearly revenue

def quarterly_revenue(request):
    today = datetime.now().date()
    current_quarter = (today.month - 1) // 3 + 1
    start_of_quarter = datetime(today.year, 3 * current_quarter - 2, 1)
    end_of_quarter = start_of_quarter.replace(month=start_of_quarter.month + 2) + timedelta(days=30)
    revenue = get_revenue(start_of_quarter, end_of_quarter)
    labels = [start_of_quarter.strftime('%Y-%m-%d'), end_of_quarter.strftime('%Y-%m-%d')]
    data = [revenue]
    graph = generate_graph(data, labels, 'Quarterly Revenue')
    return render(request, 'revenue.html', {'revenue': revenue, 'graph': graph})

def half_yearly_revenue(request):
    today = datetime.now().date()
    start_of_year = today.replace(month=1, day=1)
    mid_of_year = start_of_year.replace(month=7, day=1) + timedelta(days=6)
    end_of_year = mid_of_year.replace(month=12, day=31) + timedelta(days=5)
    if today < mid_of_year:
        start_of_period = start_of_year
        end_of_period = mid_of_year
    else:
        start_of_period = mid_of_year
        end_of_period = end_of_year
    revenue = get_revenue(start_of_period, end_of_period)
    labels = [start_of_period.strftime('%Y-%m-%d'), end_of_period.strftime('%Y-%m-%d')]
    data = [revenue]
    graph = generate_graph(data, labels, 'Half-Yearly Revenue')
    return render(request, 'revenue.html', {'revenue': revenue, 'graph': graph})

def yearly_revenue(request):
    today = datetime.now().date()
    start_of_year = today.replace(month=1, day=1)
    end_of_year = start_of_year.replace(month=12, day=31) + timedelta(days=5)
    revenue = get_revenue(start_of_year, end_of_year)
    labels = [start_of_year.strftime('%Y-%m-%d'), end_of_year.strftime('%Y-%m-%d')]
    data = [revenue]
    graph = generate_graph(data, labels, 'Yearly Revenue')
    return render(request, 'revenue.html', {'revenue': revenue, 'graph': graph})
