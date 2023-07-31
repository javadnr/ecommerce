from . import views
from django.urls import path


urlpatterns = [
    path('',views.ProductList.as_view(),name='product_list'),
    path('user/',views.UserList.as_view(),name='user_list'),
    path("detail/<int:pk>/",views.ProductDetail.as_view(),name="product_detail" ),
    path("update/<int:pk>/",views.ProductUpdate.as_view(),name="product_update" ),
    path("delete/<int:pk>/",views.ProductDelete.as_view(),name="product_delete" ),
    path("edit/<int:pk>/",views.ProductEdit.as_view(),name="product_edit" ),
    path("user/<int:pk>",views.UserEdit.as_view(),name='user_edit'),
]
