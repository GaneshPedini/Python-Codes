from django import forms
from store.models.products import Product

# creating a form
class SingleInventoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'qty_purchased', 'qty_available', 'qty_sold', 'category', 'image']
    #single_inv = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    #product_name = forms.CharField(max_length=200)
    #product_category = forms.CharField(max_length=200)
    #price = forms.IntegerField() #help_text="Enter 6 digit roll number")
    #quantity_purchased = forms.IntegerField()  # help_text="Enter 6 digit roll number")
    #quantity_sold = forms.IntegerField()
    #quantity_available = forms.IntegerField()
    #image = forms.ImageField()

class BulkInventoryForm(forms.ModelForm):
    bulk_inv = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    title = forms.CharField(max_length=50)
    file = forms.FileField()

