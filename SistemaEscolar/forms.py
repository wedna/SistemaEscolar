from django import forms
from SistemaEscolar.models import Aluno, Endereco, Funcionario, Matricula, Observacao

class AlunoForm(forms.ModelForm):
	class Meta: 
		model = Aluno
		fields = ('nome', 'email', 'cpf','nascimento',  'contato')

		widgets = {
		'nome':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.EmailInput(attrs={'class':'form-control'}),
		'cpf':forms.TextInput(attrs={'class':'form-control'}),
		'nascimento':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
		'contato':forms.TextInput(attrs={'class':'form-control'}),
		}

class FuncionarioForm(forms.ModelForm):  
	class Meta:  
		model = Funcionario
		fields = ('nome', 'email', 'cpf', 'contato', 'usuario', 'salario', 'data_contratacao' )

		widgets = {
			'nome':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'cpf':forms.TextInput(attrs={'class':'form-control'}),
			'contato':forms.TextInput(attrs={'class':'form-control'}),
			'usuario':forms.Select(attrs={'class':'form-control'}),
			'salario':forms.TextInput(attrs={'class':'form-control'}),
			'data_contratacao':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
		}		

 
class EnderecoForm(forms.ModelForm):
	class Meta:
			
		model = Endereco
		fields = ('cep', 'cidade', 'rua', 'uf', 'bairro', 'numero')
		widgets ={
			'cep':forms.TextInput(attrs={'class':'form-control', 'id':'cep'}),
			'uf':forms.Select(attrs={'class':'form-control', 'id':'uf'}),
			'cidade':forms.TextInput(attrs={'class':'form-control', 'id':'cidade'}),
			'rua':forms.TextInput(attrs={'class':'form-control'}),
			'bairro':forms.TextInput(attrs={'class':'form-control'}),
			'numero':forms.TextInput(attrs={'class':'form-control'}),

		}


class MatriculaForm(forms.ModelForm):
	class Meta:
		
		model = Matricula
		fields = ('data', 'matricula','aluno', 'turma', 'turno', 'anexos', 'observacao', 'status')

		widgets = {
			'data':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),		
			'matricula':forms.TextInput(attrs={'class':'form-control'}),
			'aluno':forms.Select(attrs={'class':'form-control'}),
			'turma':forms.Select(attrs={'class':'form-control'}),
			'turno':forms.Select(attrs={'class':'form-control'}),
			'anexos':forms.FileInput(attrs={'class' : 'form-control' }),
			'observacao': forms.TextInput(attrs={'class':'form-control'}),
			'status': forms.Select(attrs={'class':'from-control'}),
	}

class ObservacaoForm(forms.ModelForm):
	class Meta:
		model = Observacao
		fields= ('status',)

		widgets={
			'status': forms.Select(attrs={'class':'form-control'}),
		}

