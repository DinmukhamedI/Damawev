from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                        'category': category,
                        'categories': categories,
                        'products': products

                  })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',{'product': product, 'cart_product_form': cart_product_form})

def about(request):
    return render(request, 'shop/about.html')

def sign(request):
    return render(request, 'shop/sign.html')

def register(request):
    return render(request, 'shop/register.html')

def delivery(request):
    return render(request, 'shop/delivery.html')

class AddProductView(CreateView):
    model = Product
    # form_class = ProductForm
    template_name = 'shop/crud/create.html'
    fields = '__all__'

class UpdateProductView(UpdateView):
    model = Product
    template_name = 'shop/crud/update.html'
    fields = '__all__'

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'shop/crud/delete.html'
    success_url = reverse_lazy('shop:product_list')


