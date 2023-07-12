from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Snack
# Create your views here.
class HomeView(TemplateView):
    template_name='home.html'

class ThingsListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = "data"

class ThingDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack  