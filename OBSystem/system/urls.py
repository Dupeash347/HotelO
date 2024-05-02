
from django.urls import path
from .import views

urlpatterns = [
    path('', views.prehome, name='prehome'),
    path('homepage', views.homepage, name='homepage'),
    path('orders', views.orders, name='orders'),
    path("add_to_order", views.add_to_order, name='add_to_order'),
    path("remove_from_order", views.remove_from_order, name='remove_from_order'),
    path("pay", views.pay, name='pay'),
    path('complete_payment/', views.complete_payment, name='complete_payment'),
    
    #Revenue 
    path('daily-revenue/', views.daily_revenue, name='daily_revenue'),
    path('weekly-revenue/', views.weekly_revenue, name='weekly_revenue'),
    path('monthly-revenue/', views.monthly_revenue, name='monthly_revenue'),
    path('quarterly-revenue/', views.quarterly_revenue, name='quarterly_revenue'),
    path('half-yearly-revenue/', views.half_yearly_revenue, name='half_yearly_revenue'),
    path('yearly-revenue/', views.yearly_revenue, name='yearly_revenue'),
]
