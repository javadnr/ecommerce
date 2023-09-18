from django.urls import path
from .views import ItemListView, ItemDetailView, ItemDeleteView,ItemCreateView, ItemUpdateView, CommentView
from . import views

urlpatterns = [
    path('',ItemListView.as_view(),name='list'),
    path('detail/<slug:slug>/',ItemDetailView.as_view(),name='item_detail'),
    path('delete/<slug:slug>/',ItemDeleteView.as_view(),name='delete'),
    path('create_item',ItemCreateView.as_view(),name='create_item'),
    path('update/<slug:slug>',ItemUpdateView.as_view(),name='update_item'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<slug:slug>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<slug:slug>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<slug:slug>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('serach/',views.searchview,name='search'),
    path('<slug:slug>/comment/',CommentView.as_view(), name="comment"),
    
]
