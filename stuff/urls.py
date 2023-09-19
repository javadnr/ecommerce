from django.urls import path
from .views import ItemListView, ItemDetailView, ItemDeleteView,ItemCreateView, ItemUpdateView, CommentView
from . import views

urlpatterns = [
    path('',ItemListView.as_view(),name='list'),
    path('detail/<int:pk>/',ItemDetailView.as_view(),name='item_detail'),
    path('delete/<int:pk>/',ItemDeleteView.as_view(),name='delete'),
    path('create_item',ItemCreateView.as_view(),name='create_item'),
    path('update/<int:pk>',ItemUpdateView.as_view(),name='update_item'),
    path('serach/',views.searchview,name='search'),
    path('<int:pk>/comment/',CommentView.as_view(), name="comment"),
    
]
