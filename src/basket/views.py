from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Tea
from .basket import Basket
from .forms import BasketAddProductForm


@require_POST
def basket_add(request, id):
    basket = Basket(request)
    product = get_object_or_404(Tea, id=id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(product=product,
                   count=form.cleaned_data['count'],
                   update_count=form.cleaned_data['update'])

    return redirect('basket:basket_detail_url')


def basket_remove(request, id):
    basket = Basket(request)
    product = get_object_or_404(Tea, id=id)
    basket.remove(product)
    return redirect('basket:basket_detail_url')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'detail.html', context={'basket': basket})
