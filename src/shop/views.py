from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Tea, TeaType
from basket.forms import BasketAddProductForm


class TeaList(ListView):
    model = Tea
    template_name = 'index.html'
    context_object_name = 'teas'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        types = TeaType.objects.all()
        context['types'] = types
        return context


class CurrentTeaList(ListView):
    model = Tea
    template_name = 'current_tea_list.html'
    context_object_name = 'teas'
    paginate_by = 2

    def get_queryset(self):
        tea_type = get_object_or_404(TeaType, pk=self.kwargs.get('pk'))
        return Tea.objects.filter(type=tea_type)


class TeaDetail(DetailView):
    model = Tea
    template_name = 'tea_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BasketAddProductForm()
        return context
