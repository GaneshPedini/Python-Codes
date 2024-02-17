from django import forms


# creating a form
class InventoryForm(forms.Form):
    product_name = forms.CharField(max_length=200)
    product_category = forms.CharField(max_length=200)
    price = forms.IntegerField() #help_text="Enter 6 digit roll number")
    quantity_purchased = forms.IntegerField()  # help_text="Enter 6 digit roll number")
    quantity_sold = forms.IntegerField()
    quantity_available = forms.IntegerField()

