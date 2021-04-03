from django.contrib import admin
from .models import Aluno, Endereco, Funcionario, Matricula, Turma, Turno


# Register your models here.
admin.site.register(Aluno)
admin.site.register(Endereco)
admin.site.register(Funcionario)
admin.site.register(Matricula)
admin.site.register(Turma)
admin.site.register(Turno)
