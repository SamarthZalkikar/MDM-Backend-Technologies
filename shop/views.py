from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product, Order, OrderItem
from .forms import CheckoutForm


def get_cart(request):
    return request.session.get("cart", {})


def save_cart(request, cart):
    request.session["cart"] = cart
    request.session.modified = True


def cart_items_and_total(cart):
    items = []
    total = Decimal("0")
    for pid, qty in cart.items():
        try:
            product = Product.objects.get(id=int(pid))
        except (Product.DoesNotExist, ValueError):
            continue
        subtotal = product.price * qty
        total += subtotal
        items.append({"product": product, "quantity": qty, "subtotal": subtotal})
    return items, total


def product_list(request):
    query = request.GET.get("q", "")
    products = Product.objects.all().order_by("-created_at")
    if query:
        products = products.filter(name__icontains=query)
    return render(request, "shop/product_list.html", {"products": products, "query": query})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})


def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_cart(request)
    cart[str(product.id)] = cart.get(str(product.id), 0) + 1
    save_cart(request, cart)
    messages.success(request, f"Added {product.name} to cart.")
    return redirect("cart_view")


def cart_remove(request, pk):
    cart = get_cart(request)
    cart.pop(str(pk), None)
    save_cart(request, cart)
    messages.info(request, "Item removed from cart.")
    return redirect("cart_view")


def cart_update(request, pk):
    if request.method == "POST":
        qty = int(request.POST.get("quantity", 1))
        cart = get_cart(request)
        if qty <= 0:
            cart.pop(str(pk), None)
        else:
            cart[str(pk)] = qty
        save_cart(request, cart)
    return redirect("cart_view")


def cart_view(request):
    cart = get_cart(request)
    items, total = cart_items_and_total(cart)
    return render(request, "shop/cart.html", {"items": items, "total": total})


def checkout(request):
    cart = get_cart(request)
    items, total = cart_items_and_total(cart)
    if not items:
        messages.warning(request, "Your cart is empty.")
        return redirect("product_list")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total = total
            order.save()
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"],
                    price=item["product"].price,
                )
            save_cart(request, {})
            return render(request, "shop/success.html", {"order": order})
    else:
        form = CheckoutForm()

    return render(request, "shop/checkout.html", {"form": form, "items": items, "total": total})
