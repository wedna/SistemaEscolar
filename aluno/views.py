from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required #funçao para segurança do sistema
from SistemaEscolar.models import Aluno, Endereco, Turma, Turno, Matricula
from SistemaEscolar.forms import AlunoForm, EnderecoForm, ObservacaoForm
from aluno.forms import MatriculaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group #seleciona os grupo de acesso

# Create your views here.

@login_required(login_url='login_usuario') #só autentica se for usuario cadastrado como aluno.
def home(request):
	if Aluno.objects.filter(usuario_id=request.user.id).exists(): #se for usuario do grupo de aluno entra
		aluno = Aluno.objects.get(usuario_id=request.user.id)

		if Matricula.objects.filter(aluno_id=aluno.id).exists(): #exibe a matricula para o usuario logado.
			matricula = Matricula.objects.filter(aluno_id=aluno.id)
			return render(request, 'aluno/home.html', {'matricula':matricula})

		return render(request, 'aluno/home.html', {})
		
	return redirect(logout_usuario)#se não for usuario do grupo de aluno, sai do sistema.

def novo_usuario(request):
	if request.method == 'POST':
		form_usuario = UserCreationForm(request.POST)

		if form_usuario.is_valid():
		    user = form_usuario.save(commit=False)
		    grupo = get_object_or_404(Group, name='Aluno')
		    form_usuario.save()
		    user.groups.add(grupo)
		    return redirect(cadastro_aluno)
	else:
	    form_usuario = UserCreationForm()
	return render(request, 'aluno/novo_usuario.html', {'form_usuario':form_usuario})

@login_required(login_url='login_usuario')
def cadastro_aluno(request):
	if request.method =='POST':
		alunoform=AlunoForm(request.POST, request.FILES)

		if alunoform.is_valid():

			aluno=alunoform.save(commit=False)
			
			aluno.usuario_id = request.user.id	
				
			alunoform.save()
			
			
			
			return redirect(cadastrar_endereco, id=aluno.id)
	else:
		
		alunoform = AlunoForm()
	return render(request,'aluno/cadastro_aluno.html', {'alunoform': alunoform})

@login_required(login_url='login_usuario')
def cadastrar_endereco(request, id):
	aluno = get_object_or_404(Aluno, pk=id)

	if request.method=='POST':
		enderecoform=EnderecoForm(request.POST, request.FILES)
		if enderecoform.is_valid():
			endereco = enderecoform.save(commit=False)
			endereco.pessoa_id = aluno.id
			endereco.save()
			return render(request, 'aluno/home.html', {'aluno': aluno})#direcionar para tela inicial

	else:
		enderecoform= EnderecoForm()
	return render(request, 'aluno/cadastrar_endereco.html',{'enderecoform': enderecoform, 'aluno': aluno})


def login_usuario(request):
	return render(request, 'aluno/login.html', {})

def logout_usuario(request):
	logout(request)
	return render(request, 'aluno/login.html', {})



def autenticar_usuario(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	
	if user is not None:
		login(request, user)

		if Aluno.objects.filter(usuario_id=request.user.id).exists():
			return redirect(home)
		else:
			return redirect(cadastro_aluno)
	else:
		return render(request, 'aluno/login.html',{})


@login_required(login_url='login_usuario')
def solicitar_matricula(request):
	aluno=Aluno.objects.get(usuario_id=request.user.id)
	if aluno is not None:

		if request.method =='POST':
			
			matriculaform=MatriculaForm(request.POST, request.FILES)

			if matriculaform.is_valid():

				matricula=matriculaform.save(commit=False)	
				matricula.aluno_id=aluno.id
				matricula.status='PENDENTE'		
				matricula.save()						
				return redirect(home)


		else:
			
			matriculaform = MatriculaForm()
		return render(request,'aluno/solicitar_matricula.html', {'matriculaform': matriculaform})
	return redirect(home)

#def consulta	

@login_required(login_url='login_usuario')
def observacao(request):
	if request.method == 'POST':
		observacaoform= ObservacaoForm(request.POST, request.FILES)
		aluno = get_object_or_404(Aluno, usuario_id = request.user.id)
		
		if observacaoform.is_valid() and aluno is not None :

			observacao=observacaoform.save(commit=False)
			observacao.aluno_id = aluno.id
			observacao.save()
			return redirect(home)
	else:
		observacaoform=ObservacaoForm()
	return render(request, 'aluno/observacao.html', {'observacaoform': observacaoform})	
			

			 
@login_required(login_url='login_usuario')
def matricula(request):

	aluno=get_object_or_404(Aluno, usuario_id=request.user.id)
	if Matricula.objects.filter(aluno_id=aluno.id).exists():
		matricula=Matricula.objects.filter(aluno_id=aluno.id)
		
		return render(request, 'aluno/matricula.html',{'matricula': matricula, 'possui':True})
	else:
		return render(request, 'aluno/matricula.html',{ 'possui': False})


@login_required(login_url='login_usuario')
def editar_dados(request, id):
	aluno= get_object_or_404(Aluno,pk=id)
	if request.method == 'POST':
		alunoform=AlunoForm(request.POST, request.FILES, instance=aluno)
		if alunoform.is_valid():
			
			aluno=alunoform.save(commit=False)
			alunoform.save() 
			
			return redirect(dados, id=aluno.id)

	else:
		
		alunoform = AlunoForm(instance=aluno)
	return render(request,'aluno/cadastrar_aluno.html', {'alunoform': alunoform})

@login_required(login_url='login_usuario')
def endereco_editar(request,id):
	endereco=get_object_or_404(Endereco, aluno_id=id)
	if request.method=='POST':
		enderecoform=EnderecoForm(request.POST, request.FILES,instance=endereco)
		if enderecoform.is_valid():
			endereco=endercoform.save(commit=false)
			enderecoform.save()
			aluno.endereco_id=endereco.id
			return redirect(detalhes_endereco, id=endreco.id)

		else:
			enderecoform = EnderecoForm(instance=endereco)
		return render(request, 'aluno/listar_endereco.html',{'enderecoform': enderecoform})	


