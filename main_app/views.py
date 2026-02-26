from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from decimal import Decimal

from .models import Product, Customer, Order, OrderItem
from .forms import ProductForm, CustomerForm, OrderForm, OrderItemFormSet


# def home(request):
#     return render(request, 'base.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")  # your login template


def logout_view(request):
    logout(request)
    return redirect('login')


def dashboard_view(request):
    # Protect dashboard, only logged-in users
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, "home.html")  # your main dashboard template


@login_required(login_url="login")
def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "products/list.html", {"products": products})


@login_required(login_url="login")
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/detail.html", {"product": product})


@login_required(login_url="login")
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "products/form.html", {"form": form, "title": "Add Product"})


@login_required(login_url="login")
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, "products/form.html", {"form": form, "title": "Edit Product"})


@login_required(login_url="login")
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "products/confirm_delete.html", {"product": product})

@login_required(login_url="login")
def customer_list(request):
    customers = Customer.objects.all().order_by("-created_at")
    return render(request, "customers/list.html", {"customers": customers})


@login_required(login_url="login")
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, "customers/detail.html", {"customer": customer})


@login_required(login_url="login")
def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerForm()

    return render(request, "customers/form.html", {"form": form, "title": "Add Customer"})


@login_required(login_url="login")
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_detail", pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)

    return render(request, "customers/form.html", {"form": form, "title": "Edit Customer"})


@login_required(login_url="login")
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")
    return render(request, "customers/confirm_delete.html", {"customer": customer})


@login_required(login_url="login")
def order_list(request):
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "orders/list.html", {"orders": orders})


@login_required(login_url="login")
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "orders/detail.html", {"order": order})


@login_required(login_url="login")
def order_create(request):
    orders = Order.objects.all().order_by("-created_at")
    if request.method == "POST":
        form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                total_amount = Decimal(0)
                
                order_items = []
                for item_form in formset:
                    if item_form.cleaned_data:
                        item = item_form.save(commit=False)
                        item.price = item.product.price
                        total_amount += item.product.price * item.quantity
                        order_items.append(item)

                        # Subtract from inventory
                        product = item.product
                        product.quantity -= item.quantity
                        product.save()

                order.total_amount = total_amount
                order.save()
                
                for item in order_items:
                    item.order = order
                    item.save()

            return redirect("order_list")
    else:
        form = OrderForm()
        formset = OrderItemFormSet(queryset=OrderItem.objects.none())

    return render(request, "orders/form.html", {"form": form, "formset": formset, "title": "Add Order", "orders": orders})


@login_required(login_url="login")
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    orders = Order.objects.all().order_by("-created_at")
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, queryset=OrderItem.objects.filter(order=order))
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                total_amount = Decimal(0)
                
                formset.save(commit=False)
                
                for item_form in formset.cleaned_data:
                    if item_form:
                        item = item_form['id']
                        if item is None:
                            item = OrderItem(order=order)

                        # Add back to inventory the old quantity
                        if item.pk:
                            old_item = OrderItem.objects.get(pk=item.pk)
                            old_product = old_item.product
                            old_product.quantity += old_item.quantity
                            old_product.save()

                        item.product = item_form['product']
                        item.quantity = item_form['quantity']
                        item.price = item.product.price
                        item.save()
                        
                        total_amount += item.product.price * item.quantity

                        # Subtract from inventory the new quantity
                        product = item.product
                        product.quantity -= item.quantity
                        product.save()

                for obj in formset.deleted_objects:
                    product = obj.product
                    product.quantity += obj.quantity
                    product.save()
                    obj.delete()

                order.total_amount = total_amount
                order.save()

            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(queryset=OrderItem.objects.filter(order=order))

    return render(request, "orders/form.html", {"form": form, "formset": formset, "title": "Edit Order", "orders": orders})


@login_required(login_url="login")
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        with transaction.atomic():
            for item in order.items.all():
                product = item.product
                product.quantity += item.quantity
                product.save()
            order.delete()
        return redirect("order_list")
    return render(request, "orders/confirm_delete.html", {"order": order})
