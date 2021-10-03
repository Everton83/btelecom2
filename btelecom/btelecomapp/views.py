from django.db.models.query_utils import select_related_descend
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from.models import *
from django.http import HttpResponse, request

# Create your views here.

class HomeView(ListView):
    template_name = "home.html"
    model = Solucoes
    context_object_name = 'home'
    paginate_by = 3
    queryset = Solucoes.objects.all().order_by("-criado_em")

class SearchResultsView(ListView):
    template_name = "search_results.html"
    model = Solucoes
    context_object_name = 'search_results'
    paginate_by = 10
    queryset = Solucoes.objects.all().order_by("-criado_em")
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Solucoes.objects.filter(
            Q(porta1__icontains=query)
        ).order_by("-criado_em")
        return object_list

class FormView(ListView):
    template_name = "form.html"
    model = Solucoes
    context_object_name = 'form'
    queryset = Solucoes.objects.all().order_by("-criado_em")
    
class SearchView(ListView):
    template_name = "dataform.html"
    model = Solucoes
    context_object_name = 'SearchView'
    paginate_by = 10
    queryset = Solucoes.objects.all().order_by("-criado_em")
    def SearchView(request):
        porta1=(request.GET.get('id_porta1'))
        porta2=(request.GET.get('id_porta2'))
        porta3=(request.GET.get('id_porta3'))
        porta4=(request.GET.get('id_porta4'))
        porta5=(request.GET.get('id_porta5'))
        porta6=(request.GET.get('id_porta6'))
        object_list = Solucoes.objects.filter(
            Q(porta1=porta1) | Q(porta2=porta2) | Q(porta3=porta3) | Q(porta4=porta4) | Q(porta5=porta5) | Q(porta5=porta6)
        ).order_by("-criado_em")
        print(porta1)
        return object_list