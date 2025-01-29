from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, ContactPerson
from .forms import CustomerForm, ContactPersonForm
from django.contrib import messages



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers:list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})

def edit_customer(request, id):
    print("Rendering template: customers/customer_edit.html")  # Debug statement
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_edit.html', {'form': form, 'customer': customer})

def read_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        customer.delete()
        return redirect('customers:list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully!")
            return redirect('customers:list')  # Replace with the name of your customer list view
    else:
        form = CustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})


# Existing views above...

def home_view(request):
    return render(request, 'customers/home.html')  # we'll create home.html next



# ... existing customer views above ...

def contactperson_list(request):
    contacts = ContactPerson.objects.select_related('customer').all()
    return render(request, 'customers/contactperson_list.html', {'contacts': contacts})


def create_contactperson(request):
    if request.method == "POST":
        form = ContactPersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Person added successfully!")
            return redirect('customers:contactperson_list')
    else:
        form = ContactPersonForm()
    return render(request, 'customers/contactperson_form.html', {'form': form})


def edit_contactperson(request, id):
    contact = get_object_or_404(ContactPerson, id=id)
    if request.method == "POST":
        form = ContactPersonForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Person updated successfully!")
            return redirect('customers:contactperson_list')
    else:
        form = ContactPersonForm(instance=contact)
    return render(request, 'customers/contactperson_edit.html', {'form': form, 'contact': contact})


def read_contactperson(request, id):
    contact = get_object_or_404(ContactPerson, id=id)
    return render(request, 'customers/contactperson_detail.html', {'contact': contact})


def delete_contactperson(request, id):
    contact = get_object_or_404(ContactPerson, id=id)
    if request.method == "POST":
        contact.delete()
        messages.success(request, "Contact Person deleted successfully!")
        return redirect('customers:contactperson_list')
    return render(request, 'customers/contactperson_confirm_delete.html', {'contact': contact})


def add_contactperson(request):
    """Add a new Contact Person."""
    if request.method == 'POST':
        form = ContactPersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Person added successfully!")
            # Redirect where you wish after saving. Adjust the URL name accordingly.
            return redirect('contacts:contactperson_list')
    else:
        form = ContactPersonForm()

    return render(request, 'customers/add_contactperson.html', {'form': form})

