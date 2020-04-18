from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # 追加
from .forms import DayCreateForm
from .models import Day

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'diary/day_list.html'
    model = Day

class AddView(LoginRequiredMixin, generic.CreateView):     # 修正
    template_name = 'diary/day_form.html'
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class UpdateView(LoginRequiredMixin, generic.UpdateView):  # 修正
    template_name = 'diary/day_form.html'
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class DeleteView(LoginRequiredMixin, generic.DeleteView):  # 修正
    template_name = 'diary/day_confirm_delete.html'
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    template_name = 'diary/day_detail.html'
    model = Day
