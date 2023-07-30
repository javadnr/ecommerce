from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Item
from django.urls import reverse_lazy

from django.shortcuts import redirect


class ItemListView(ListView):
    model = Item
    template_name = 'stuff/list.html'
    context_object_name = 'items'
    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'stuff/detail.html'
    context_object_name = 'item'
    
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'stuff/delete.html'
    success_url = reverse_lazy('list')
    
class ItemCreateView(CreateView):
    model = Item
    template_name = 'stuff/create_item.html'
    success_url = reverse_lazy('list')
    fields = '__all__'
    
class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'stuff/update_item.html'
    fields = '__all__'
    


 
    
