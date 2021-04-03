from django import forms
from SistemaEscolar.models import Matricula


class MatriculaForm(forms.ModelForm):
	class Meta:
		
		model = Matricula
		fields = ('data', 'turma', 'turno', 'anexos', 'observacao')

		widgets = {
			'data':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),	
			'turma':forms.Select(attrs={'class':'form-control'}),
			'turno':forms.Select(attrs={'class':'form-control'}),
			'anexos':forms.FileInput(attrs={'class' : 'form-control' }),
			'observacao': forms.TextInput(attrs={'class':'form-control'}),
			
	}