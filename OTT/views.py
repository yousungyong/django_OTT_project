from typing_extensions import Self
from django.shortcuts import render
from OTT.models import movie
from django.views.generic import DetailView, ListView
from django.core.exceptions import PermissionDenied
# Create your views here.

# class Main(DetailView):
class Main(ListView):
    model = movie
    template_name = 'index.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class Detail(DetailView):
    model = movie
    template_name = 'OTT/detail.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class Play(DetailView):
    model = movie
    template_name = 'OTT/play.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


