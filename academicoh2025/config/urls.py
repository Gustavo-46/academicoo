from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('genero/', GenerosView.as_view(), name='genero'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('area_saber/', AreasSaberView.as_view(), name='area_saber'),
    path('avaliacao_tipo/', AvaliacoesTiposView.as_view(), name='avaliacao_tipo'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencia'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencia'),
    path('curso_disciplina/', CursoDisciplinaView.as_view(), name='curso_disciplina'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
]
