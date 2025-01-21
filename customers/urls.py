from django.urls import path
from . import views
from .views import add_customer

app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='list'),
    path('create/', views.create_customer, name='create'),
    path('<int:id>/edit/', views.edit_customer, name='edit'),
    path('<int:id>/', views.read_customer, name='read'),
    path('<int:id>/delete/', views.delete_customer, name='delete'),
    path('add/', add_customer, name='add_customer'),
    path('', views.home_view, name='home'),  # Root URL -> home_view
]
