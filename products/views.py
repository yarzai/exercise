from django.views.generic.base import View, TemplateView
from math import prod
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.db.models import Q

from products.models import Product


# Create your views here.

# list product
def list_products(request):
    # products = Product.objects.filter(
    #     Q(is_available=True) | Q(category='el'), price=13100)  # SELECT * FROM products.s
    # print(products.query)

    products = Product.objects.get_availibes()
    for p in products:
        print(p.get_price)
    return render(request, 'products/list-products.html', {'products': products})


# Create product
def create_product(request):
    if request.method == "GET":
        return render(request, 'products/create-product.html')
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available')
        category = request.POST.get('category')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        product = Product.objects.create(
            name=name, price=price,
            is_available=bool(is_available),
            category=category,
            description=desc,
            image=image
        )

        # product.price = float(product.price) +  100
        # product.save()

        return redirect(reverse_lazy('products:list'))


# update product
def update_product(request, prod_slug):
    if request.method == 'GET':
        product = Product.objects.get(slug=prod_slug)
        return render(request, 'products/update-product.html', {'product': product})
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available')
        category = request.POST.get('category')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        product = Product.objects.get(slug=prod_slug)

        product.name = name
        product.price = price
        product.is_available = bool(is_available)
        product.category = category
        product.description = desc

        if image:
            if os.path.exists(product.image.path):
                os.remove(product.image.path)
            product.image = image

        product.save()

        return redirect(reverse_lazy('products:update', args=[prod_slug]))
        # return HttpResponse(f"Update id - {product.id} - {product.created}")

# delete product


def delete_product(request, prod_slug):
    product = Product.objects.get(slug=prod_slug)

    if os.path.exists(product.image.path):
        os.remove(product.image.path)

    product.delete()

    return HttpResponse(f"Deleted {prod_slug}")


@login_required
def show_news(request):
    print("request", request.path)
    return HttpResponse("Welcome to Django")


@login_required
def home(request):

    #print("request", dir(request))
    # print(request.path)

    # if request.user.is_authenticated:
    return render(request, 'index.html', {"title": "Hello World 2", "name": "Ahmad"})
    # else:
    #     return HttpResponse("Please Login to access this page.")


def product_detail(request, prod_slug):
    product = Product.objects.get(slug=prod_slug)
    return render(request, 'products/product-detail.html', {'product': product})


# class ListProduct(View):
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()

#         return render(request, 'products/list-products.html', {'products': products})
class ListProduct(TemplateView):
    # template_name = 'about.html'

    # def get_template_names(self):

    #     return ['about.html']

    pass
