from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Contact

def home(request):
    return render(request, 'core/home.html')

def products(request):
    items = Product.objects.all()
    return render(request, 'core/products.html', {'products': items})

def services(request):
    return render(request, 'core/services.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
    return render(request, 'core/contact.html')
def products(request):
    menu_categories = [
        ("Coffee", Product.objects.filter(category='coffee')),
        ("Cold Beverages", Product.objects.filter(category='cold')),
        ("Snacks", Product.objects.filter(category='snack')),
        ("Desserts", Product.objects.filter(category='dessert')),
    ]
    return render(request, 'core/products.html', {'menu_categories': menu_categories})

# Add to Cart
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
    request.session['cart'] = cart
    return redirect('view_cart')

# Remove from Cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
    request.session['cart'] = cart
    return redirect('view_cart')

# View Cart
def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'core/cart.html', {'products': products})
