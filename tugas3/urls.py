from django.urls import path
from . import views

urlpatterns = [
    path('item-list/', views.item_list, name='item-list'),
]
