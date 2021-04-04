from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):
	nome = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
	cpf = models.CharField(max_length=20, null=True, blank=True, unique=True)
	contato = models.CharField(max_length=100, null=True, blank=True)
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)

	def __str__(self):
		return self.nome

class Aluno(Pessoa):
	nascimento = models.DateField(null=True, blank=True)
	
class Funcionario(Pessoa):

	salario = models.FloatField(max_length=20, null=True, blank=True)
	data_contratacao = models.DateField(null=True, blank=True)
		


class Endereco(models.Model):
	uf_choices = [
			('AC', 'Acre'),
			('PI', 'Piauí'),
			('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MG', 'Minas Gerais'),
            ('MS', 'Mato Grosso do Sul'),
            ('MT', 'Mato Grosso'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PE', 'Pernanbuco'),
            ('PI', 'Piauí'),
            ('PR', 'Paraná'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('RS', 'Rio Grande do Sul'),
            ('SC', 'Santa Catarina'),
            ('SE', 'Sergipe'),
            ('SP', 'São Paulo'),
            ('TO', 'Tocantins')
           ]
	cep = models.CharField(max_length=10)
	uf = models.CharField(max_length=2, choices=uf_choices)
	cidade = models.CharField(max_length=100)
	bairro = models.CharField(max_length=20)
	numero = models.CharField(max_length=10)
	rua = models.CharField(max_length=20)
	pessoa = models.OneToOneField(Pessoa, blank=True, null=True, on_delete=models.CASCADE)


			
	def __str__(self):
		return self.rua



class Turma(models.Model):
	turma = models.CharField(max_length=20)
	codigo = models.CharField(max_length=20)

	def __str__(self):																		
		return self.turma	



class Turno(models.Model):
	turno = models.CharField(max_length=10)

	def __str__(self):
		return self.turno



class Matricula(models.Model):
	status_choices=[
			('PENDENTE', 'PENDENTE'),
			('CONCLUÍDA', 'CONCLUÍDA'),
			('CANCELADA', 'CANCELADA'),
			('RECUSADA', 'RECUSADA')

			]
	data = models.DateTimeField(auto_now_add=False, blank=True, null=True)
	matricula= models.CharField(max_length=20, null=True, blank=True, unique=True)
	
	aluno = models.ForeignKey(Aluno, blank=True, null=True, on_delete=models.CASCADE)
	turma= models.ForeignKey(Turma, blank=True, null=True, on_delete=models.CASCADE)
	turno = models.ForeignKey(Turno, blank=True, null=True, on_delete=models.CASCADE)
	anexos = models.FileField(upload_to = "SistemaEscolar/doc", blank = True, null= True)
	observacao = models.TextField(blank=True, null=True)
	status = models.CharField(max_length=20, null=True, choices=status_choices, default='PENDENTE')

	def __str__(self):
		return self.matricula

class Observacao(models.Model):
	status_choices=[
			('PENDENTE', 'PENDENTE'),
			('CONCLUÍDA', 'CONCLUÍDA'),
			
			]
	aluno = models.ForeignKey(Aluno, blank=True, null=True, on_delete=models.CASCADE)
	observacao = models.TextField(blank=True, null=True)
	data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	status = models.CharField(max_length=20, null=True, choices=status_choices, default='PENDENTE')




															