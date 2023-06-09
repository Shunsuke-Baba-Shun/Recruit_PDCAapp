from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import reflection

class PDCAListView(LoginRequiredMixin, ListView):
    template_name = 'pdca/pdca_list.html'
    model = reflection

class PDCADetailView(LoginRequiredMixin, DetailView):
    template_name = 'pdca/pdca_detail.html'
    model = reflection

class PDCACreateView(LoginRequiredMixin, CreateView):
    template_name = 'pdca/pdca_create.html'
    model = reflection
    fields = ('title', 'description', 'Category', 'Plan', 'Do', 'Check', 'Action')
    success_url = reverse_lazy('pdca-list')

class PDCADeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'pdca/pdca_delete.html'
    model = reflection
    success_url = reverse_lazy('pdca-list')

class PDCAUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'pdca/pdca_update.html'
    model = reflection
    fields = ('title', 'description', 'Category', 'Plan', 'Do', 'Check', 'Action')
    success_url = reverse_lazy('pdca-list')

def PDCAIndexView(request):
    object_list = reflection.objects.order_by('Category')
    return render(request, 'pdca/pdca_index.html', {'object_list': object_list})
