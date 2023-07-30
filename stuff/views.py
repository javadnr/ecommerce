from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Product
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


class ItemListView(ListView):
    model = Product
    template_name = 'stuff/list.html'
    context_object_name = 'products'
    
class ItemDetailView(DetailView):
    model = Product
    template_name = 'stuff/detail.html'
    context_object_name = 'product'
    
class ItemDeleteView(DeleteView):
    model = Product
    template_name = 'stuff/delete.html'
    success_url = reverse_lazy('list')
    
class ItemCreateView(CreateView):
    model = Product
    template_name = 'stuff/create_item.html'
    success_url = reverse_lazy('list')
    fields = '__all__'
    
class ItemUpdateView(UpdateView):
    model = Product
    template_name = 'stuff/update_item.html'
    fields = '__all__'
    


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("list")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("list")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'stuff/cart_detail.html')