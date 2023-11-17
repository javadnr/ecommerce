from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Product, Comment, Cart, CartItem
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CartItemForm


class ItemListView(ListView):
    model = Product
    template_name = 'stuff/list.html'
    context_object_name = 'products'
    ordering = ['-date_added'] 
  
    
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
    fields = ['name', 'discription','image','price']


class CommentView(CreateView):
    model = Comment
    template_name = 'stuff/comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('list')
    ordering = ['-date_added'] 
        
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


def searchview(request):
    if request.method == "GET":
        searched = request.GET['searched']
        products = Product.objects.filter(name__icontains=searched)
        return render(request, "stuff/search.html", {'searched': searched,
                                                     'products': products}
                      )
    else: 
        return render(request, "stuff/search.html",{'searched' :searched} )


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart,product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('cart')


def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()

    return render(request, 'stuff/cart.html', {'cart_items': cart_items})


def update_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')
