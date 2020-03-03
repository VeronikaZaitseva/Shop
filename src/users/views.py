from django.shortcuts import render, redirect
from .forms import UserRegisterForm, BuyerRegisterForm
from django.contrib import messages
from .models import Buyer


def register(request):
    if request.method == 'POST':
        form_user = UserRegisterForm(request.POST)
        form_buyer = BuyerRegisterForm(request.POST)
        if form_buyer.is_valid() and form_user.is_valid():
            user = form_user.save()
            buyer = Buyer.objects.create(user=user, phone_number=form_buyer.cleaned_data.get('phone_number'))
            username = form_user.cleaned_data['username']
            messages.success(request, f'Account created for {username}')
            return redirect('login_url')
    else:
        form_user = UserRegisterForm()
        form_buyer = BuyerRegisterForm()
        return render(request, 'register.html', context={'form_user': form_user, 'form_buyer': form_buyer})
