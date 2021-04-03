#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login', views.login_usuario, name='login_usuario'),
    path('autenticar_aluno', views.autenticar_usuario, name='autenticar_aluno'),
    path('logout', views.logout_usuario, name='logout'),

    path('usuario/new/', views.novo_usuario, name='novo_usuario'),
    path('cadastrar_endereco/new/<int:id>/', views.cadastrar_endereco, name='cadastrar_endereco'),
    path('aluno/new/', views.cadastro_aluno, name='cadastro_aluno'),
    path('listar_matricula/', views.matricula, name='matricula'),
    path('matricula/new/', views.solicitar_matricula, name='solicitar_matricula'),
    #path('consulta/', views.consulta, name='consulta'),
    path('observacao/', views.observacao, name='observacao'),


]
  