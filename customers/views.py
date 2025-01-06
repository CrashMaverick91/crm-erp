from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, ContactPerson
from .forms import CustomerForm, ContactPersonForm

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
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form})

def read_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        customer.delete()
        return redirect('customers:list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})
