# customers/urls.py
from django.urls import path, include
from . import views
from .views import add_customer


app_name = 'customers'  # This is the main namespace for "customers"

urlpatterns = [
    path('', views.customer_list, name='list'),
    path('create/', views.create_customer, name='create'),
    path('<int:id>/edit/', views.edit_customer, name='edit'),
    path('<int:id>/', views.read_customer, name='read'),
    path('<int:id>/delete/', views.delete_customer, name='delete'),
    path('add/', add_customer, name='add_customer'),
    path('', views.home_view, name='home'),
]

# ------------------ Sub-URLconf for Contacts ------------------ #
contacts_urlpatterns = ([
    path('list/', views.contactperson_list, name='contactperson_list'),
    path('create/', views.create_contactperson, name='contactperson_create'),
    path('<int:id>/edit/', views.edit_contactperson, name='contactperson_edit'),
    path('<int:id>/detail/', views.read_contactperson, name='contactperson_detail'),
    path('<int:id>/delete/', views.delete_contactperson, name='contactperson_delete'),
    path('add/', views.add_contactperson, name='add_contactperson'),
], 'contacts')

urlpatterns += [
    # Attach the above sub-URLconf to /contacts/
    path('contacts/', include(contacts_urlpatterns))
]
