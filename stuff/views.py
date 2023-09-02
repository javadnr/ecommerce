from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Product, comment
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import CommentForm


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

class CommentView(CreateView):
    model = comment
    template_name = 'stuff/comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('list')
    ordering = ['-date_added'] 
    

        
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required(login_url="account_login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("list")


@login_required(login_url="account_login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="account_login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="account_login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="account_login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("list")


@login_required(login_url="account_login")
def cart_detail(request):
    return render(request, 'stuff/cart_detail.html')

def searchview(request):
    if request.method == "GET":
        searched = request.GET['searched']
        products = Product.objects.filter(name__icontains = searched)
        return render(request, "stuff/search.html",{'searched' :searched , 'products': products} )
    else: 
        return render(request, "stuff/search.html",{'searched' :searched} )
