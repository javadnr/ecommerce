from django.views.generic import ListView, DetailView
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'stuff/list.html'
    context_object_name = 'items'
    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'stuff/detail.html'
    context_object_name = 'item'
    
