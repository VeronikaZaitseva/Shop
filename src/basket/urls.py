from django.urls import path
from .views import *

app_name = 'basket'
urlpatterns = [
    path('', basket_detail, name='basket_detail_url'),
    path('add/<int:id>', basket_add, name='basket_add_url'),
    path('remove/<int:id>', basket_remove, name='basket_remove_url'),
]