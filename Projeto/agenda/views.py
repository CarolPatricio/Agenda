from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from Projeto.models import Contato
from agenda.forms import InsereContatoForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "agenda/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class ContatoListView(ListView):
    template_name = "agenda/lista.html"
    model = Contato
    context_object_name = "contatos"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class ContatoCreateView(CreateView):
    template_name = "agenda/cria.html"
    model = Contato
    form_class = InsereContatoForm
    success_url = reverse_lazy("agenda:lista_contatos")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class ContatoUpdateView(UpdateView):
    template_name = "agenda/atualiza.html"
    model = Contato
    fields = '__all__'
    context_object_name = 'contato'
    success_url = reverse_lazy("agenda:lista_contatos")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class ContatoDeleteView(DeleteView):
    template_name = "agenda/exclui.html"
    model = Contato
    context_object_name = 'contatos'
    success_url = reverse_lazy("agenda:lista_contatos")
