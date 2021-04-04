#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    
    path('', views.home_sistema, name='home_sistema'),
    #path('', views.home_sistema, name='negar_permissao'),

    path('listar_alunos', views.listar_alunos, name='listar_alunos'),
    #path('listar_endereco', views.listar_endereco, name='listar_endereco'),
    path('listar_turma', views.listar_turma, name='listar_turma'),
    path('lista_turno', views.listar_turno, name='listar_turno'),
    path('listar_matricula', views.listar_matricula, name='listar_matricula'),
    path('listar_funcionario', views.listar_funcionario, name='listar_funcionario'),
    path('aluno/<int:id>/', views.detalhes_aluno, name='detalhes_aluno'),
    path('aluno/new/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('aluno/editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('endereco/editar/<int:id>/', views.editar_endereco, name='editar_endereco'),
    path('obervacao/editar/<int:id>/', views.editar_observacao, name='editar_observacao'),


    path('buscar_aluno', views.buscar_aluno, name='buscar_aluno'),
    
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),

    path('deletar_aluno/<int:id>/', views.deletar_aluno, name='deletar_aluno'),
    path('cadastrar_funcionario/new/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar_matricula/new/', views.cadastrar_matricula, name='cadastrar_matricula'),
    path('cadastrar_endereco/new/<int:id>/', views.cadastrar_endereco, name='cadastrar_endereco'),
    path('buscar_matricula/<int:id>/', views.buscar_matricula, name='buscar_matricula'),
    path('cadastrar_usuario/new/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('matricula/editar/<int:id>/', views.editar_matricula, name='editar_matricula'),
    path('funcionario/editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),

]
 