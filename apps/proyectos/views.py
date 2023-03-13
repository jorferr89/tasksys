from audioop import reverse
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class ProyectosListView(ListView):
    model = Proyecto
    template_name = 'proyectos.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proyectos'
        return context


