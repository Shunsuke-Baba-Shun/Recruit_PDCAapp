from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import reflection

class PDCAListView(ListView):
    template_name = 'pdca/pdca_list.html'
    model = reflection

class PDCADetailView(DetailView):
    template_name = 'pdca/pdca_detail.html'
    model = reflection

class PDCACreateView(CreateView):
    template_name = 'pdca/pdca_create.html'
    model = reflection
    fields = ('title', 'description', 'Category', 'Plan', 'Do', 'Check', 'Action')
    success_url = reverse_lazy('pdca-list')

class PDCADeleteView(DeleteView):
    template_engine = 'pdca/pdca_delete.html'
    model = reflection
    success_url = reverse_lazy('pdca-list')

class PDCAUpdateView(UpdateView):
    template_name = 'pdca/pdca_update.html'