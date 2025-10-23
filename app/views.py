from django.shortcuts import render
from app import settings
import os
from django.views.generic import ListView, DetailView, CreateView
from django.http import FileResponse
from .models import MonTruc
from .forms import MonTrucForm

class truc_list_view(ListView):
    model = MonTruc
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb"] = [('Home', '/')]
        return context

class truc_detail_view(DetailView):
    model = MonTruc
    template_name = 'details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb"] = [('Home', '/'), (self.object.name, self.request.path)]
        return context

class truc_visu_view(DetailView):
    model = MonTruc
    def render_to_response(self, request):
        return FileResponse(self.object.path)

class MonTrucCreateView(CreateView):
    model = MonTruc
    form_class = MonTrucForm
    template_name = 'index.html'
    success_url = '/merci/'  # Redirection après envoi