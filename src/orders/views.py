from django.shortcuts import render
from basket.basket import Basket
from .forms import OrderCreateForm
from django.core.mail import send_mail
from datetime import datetime


def time_limit_decorator(func):
    def wrapper(request):
        now_hour = datetime.now().hour + 3
        if now_hour >= 22 or now_hour <= 8:
            return render(request, 'time_limit.html')
        else:
            return func(request)

    return wrapper


@time_limit_decorator
def order_create(request):
    basket = Basket(request)
    user = request.user
    if user.is_authenticated:
        try:
            buyer = request.user.buyer
        except:
            return render(request, 'notcustomer.html')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            basket.clear()
            send_mail(
                'Order in CandyShop',
                f'Your order number{order.id}',
                'nicusha1997@yandex.by',
                [order.email],
                fail_silently=False,
            )
            return render(request, 'created.html', context={'order': order})
        return render(request, 'create.html', context={'form': form, 'basket': basket})

    else:
        if user.is_authenticated:
            form = OrderCreateForm(instance=user, initial={'phone_number': buyer.phone_number})
        else:
            form = OrderCreateForm()
        return render(request, 'create.html', context={'form': form, 'basket': basket})
