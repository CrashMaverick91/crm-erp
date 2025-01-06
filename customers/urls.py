from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.create_customer, name='create'),
    path('<int:id>/edit/', views.edit_customer, name='edit'),
    path('<int:id>/', views.read_customer, name='read'),
    path('<int:id>/delete/', views.delete_customer, name='delete'),
]
