from django.urls import path
from .views import (
    TeaList,
    TeaDetail,
    CurrentTeaList,
)

app_name = 'shop'
urlpatterns = [
    path('', TeaList.as_view(), name='tea_list_url'),
    path('<int:pk>/detail/', TeaDetail.as_view(), name='tea_detail_url'),
    path('tea/<int:pk>', CurrentTeaList.as_view(), name='current_tea_list_url'),
]
