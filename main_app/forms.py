from django import forms
from .models import Product, Customer, Order, OrderItem
from django.forms import modelformset_factory
from django.utils import timezone


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "product_id",
            "product_name",
            "product_description",
            "price",
            "unit_of_measure",
            "quantity",
            "brand",
            "selling_price",
            "status",
        ]
        widgets = {
            "product_description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-slate-500",
            )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "registered_name",
            "business_address",
            "tin_number",
            "mobile_tel_number",
            "email_address",
        ]
        widgets = {
            "business_address": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-slate-500",
            )

class OrderForm(forms.ModelForm):
    order_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=timezone.now().date())
    class Meta:
        model = Order
        fields = [
            "customer",
            "order_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-slate-500",
            )

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "w-full rounded-lg border border-gray-300 px-3 py-2 text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-slate-500",
            )

OrderItemFormSet = modelformset_factory(
    OrderItem,
    form=OrderItemForm,
    extra=1,
    can_delete=True
)
