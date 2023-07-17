from django.urls import path
from .views import StuffDetail
urlpatterns = [
    path('detail/<int:pk>/',StuffDetail.as_view(),name='stuff_detail'),
]
