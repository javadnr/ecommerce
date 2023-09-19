from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Product, comment
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
    fields = ['name', 'discription','image','price']

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


def searchview(request):
    if request.method == "GET":
        searched = request.GET['searched']
        products = Product.objects.filter(name__icontains = searched)
        return render(request, "stuff/search.html",{'searched' :searched , 'products': products} )
    else: 
        return render(request, "stuff/search.html",{'searched' :searched} )
