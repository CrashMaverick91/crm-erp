from django.contrib import admin
from .models import Customer, ContactPerson

class ContactPersonInline(admin.TabularInline):
    model = ContactPerson
    extra = 1  # Number of empty rows to show for new entries


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'p_iva', 'email', 'phone', 'created_at')  # Corrected list_display
    inlines = [ContactPersonInline]


@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'cell', 'customer')  # This applies to the ContactPerson model
