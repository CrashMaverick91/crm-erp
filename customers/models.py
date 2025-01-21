from django.db import models

class Customer(models.Model):
    business_name = models.CharField(max_length=255, unique=True, default="Unknown")
    p_iva = models.CharField("P.IVA", max_length=20, unique=True, blank=True, null=True)
    sdi_code = models.CharField("SDI Code", max_length=20, blank=True, null=True)
    pec = models.EmailField("PEC Email", blank=True, null=True)
    email = models.EmailField("Regular Email", blank=True, null=True)
    phone = models.CharField("Telephone", max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name


class ContactPerson(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="contacts")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cell = models.CharField("Mobile Phone", max_length=15, blank=True, null=True)
    email = models.EmailField("Contact Email", blank=True, null=True)
    role = models.CharField("Role/Position", max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.customer.business_name})"

