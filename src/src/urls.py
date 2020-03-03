from django.contrib import admin
from django.urls import path, include
from users.views import register
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls', namespace='basket')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('register/', register, name='register_url'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login_url'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout_url'),

]