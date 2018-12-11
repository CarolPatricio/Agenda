from agenda.views import IndexTemplateView, ContatoListView, ContatoUpdateView, ContatoCreateView, \
    ContatoDeleteView

from django.urls import path

app_name = 'agenda'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /contato/cadastrar
    path('contato/cadastrar', ContatoCreateView.as_view(), name="cadastra_contato"),

    # GET /contato
    path('contatos/', ContatoListView.as_view(), name="lista_contatos"),

    # GET/POST /contato/{pk}
    path('contato/<pk>', ContatoUpdateView.as_view(), name="atualiza_contato"),

    # GET/POST /contatos/excluir/{pk}
    path('contato/excluir/<pk>', ContatoDeleteView.as_view(), name="deleta_contato"),
]
