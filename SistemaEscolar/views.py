from django.shortcuts import render, get_object_or_404, redirect
from SistemaEscolar.models import Aluno, Endereco, Turma, Turno, Matricula, Funcionario, Observacao
from SistemaEscolar.forms import AlunoForm, EnderecoForm, FuncionarioForm, MatriculaForm, ObservacaoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required #funçao para segurança do sistema


# Create your views here. #views de acesso dos funcionarios.
@login_required(login_url='page_login')
def home_sistema(request):
	#somente o funcionario e usuario super acessar o sistema. 
	if request.user.groups.filter(name='Funcionario').exists() or request.user.has_module_perms('Administrador'):
	#ORDENAR POR DATA E MOSTRAR NA HOME APENAS AS INFORMAÇÕES PENDENTES.
		observacao=Observacao.objects.filter(status='PENDENTE').order_by('data')
		return render(request, 'SistemaEscolar/home_sistema.html', {'observacao': observacao})
	else:
		logout(request)
		return render(request,  'SistemaEscolar/negar_permissao.html', {})


 
@login_required(login_url='page_login')
def deletar_aluno(request, id): #função destinada apenas aos funcionarios.
	aluno= get_object_or_404(Aluno,pk=id)
	if request.method=='POST':

		aluno.delete() 
		return redirect(listar_alunos)
	else:
		return render(request, 'SistemaEscolar/confirmar_delete.html', {'aluno':aluno})

	


def logout_usuario(request): #sair do sistema
	logout(request)
	return render(request, 'SistemaEscolar/login.html', {})





@login_required(login_url='page_login')
def cadastrar_usuario(request):#função para fazer seu cadastro do usuario de aluno.
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)

        if form_usuario.is_valid():
            user = form_usuario.save(commit=False)
           
            grupo = get_object_or_404(Group, name='Aluno')
            form_usuario.save()

            user.groups.add(grupo)

            return redirect(cadastrar_matricula)
    else:
        form_usuario = UserCreationForm()
    return render(request, 'SistemaEscolar/cadastrar_usuario.html', {'form_usuario':form_usuario})

    

def autenticar_usuario(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		#condição para somente o funcionario e usuario super acessar o sistema. 
		if request.user.groups.filter(name='Funcionario').exists() or request.user.has_module_perms('Administrador'):
			return redirect(home_sistema)
		else:
			logout(request)
			return render(request, 'SistemaEscolar/negar_permissao.html',{})
	else:
		return render(request, 'SistemaEscolar/login.html',{})	
		


def page_login(request): #redirecionamento para atela de login.
	return render(request, 'SistemaEscolar/login.html', {})


#função de buscar aluno por nome completo ou letra correspondente ao nome.
#função destinada apenas aos funcionarios.
@login_required(login_url='page_login')
def buscar_aluno(request): 
	info = request.POST['info'] 
	alunos = Aluno.objects.filter(nome__contains=info)
	return render(request, 'SistemaEscolar/listar_alunos.html', {'alunos': alunos})






#função destinada apenas aos funcionarios.
@login_required(login_url='page_login')
def editar_aluno(request, id):
	aluno= get_object_or_404(Aluno,pk=id)
	if request.method == 'POST': 
		alunoform=AlunoForm(request.POST, request.FILES, instance=aluno)
		if alunoform.is_valid():
			aluno=alunoform.save(commit=False)
			alunoform.save() 
			return redirect(detalhes_aluno, id=aluno.id)
	else:
		alunoform = AlunoForm(instance=aluno)
	return render(request,'SistemaEscolar/cadastrar_aluno.html', {'alunoform': alunoform})

login_required(login_url='page_login')
def editar_funcionario(request, id):
	funcionario= get_object_or_404(Funcionario,pk=id)
	if request.method == 'POST': 
		funcionarioform=FuncionarioForm(request.POST, request.FILES, instance=funcionario)
		if funcionarioform.is_valid():
			funcionario=funcionarioform.save(commit=False)
			funcionarioform.save() 
			return redirect(listar_funcionario)
	else:
		funcionarioform = FuncionarioForm(instance=funcionario)
	return render(request,'SistemaEscolar/cadastrar_funcionario.html', {'funcionarioform': funcionarioform})



def editar_matricula(request, id):
	matricula=get_object_or_404(Matricula, pk=id)
	if request.method == 'POST':
		matriculaform= MatriculaForm(request.POST, request.FILES, instance=matricula)
		if matriculaform.is_valid():
			matricula=matriculaform.save(commit=False)
			matricula.save()
			return redirect(listar_matricula)
	else:
		matriculaform = MatriculaForm(instance=matricula)
	return render (request, 'SistemaEscolar/cadastrar_matricula.html', {'matriculaform': matriculaform})			



#função destinada apenas aos funcionarios.
@login_required(login_url='page_login')
def editar_endereco(request,id):
	endereco=get_object_or_404(Endereco, pessoa_id=id) #o endereço é correspondente ao aluno via id.
	if request.method=='POST':
		enderecoform=EnderecoForm(request.POST, request.FILES,instance=endereco)
		if enderecoform.is_valid():
			endereco=endercoform.save(commit=false)
			enderecoform.save()
			aluno.endereco_id=endereco.id
			return redirect(detalhes_endereco, id=endreco.id)
		else:
			enderecoform = EnderecoForm(instance=endereco)

	else:
		enderecoform = EnderecoForm(instance=endereco)
	return render(request, 'SistemaEscolar/cadastrar_endereco.html',{'enderecoform': enderecoform})	



def editar_observacao(request,id):
	#mudar as informações de pendente para concluído.
	observacao=get_object_or_404(Observacao, pk=id)
	if request.method=='POST':
		observacaoform=ObservacaoForm(request.POST, request.FILES, instance=observacao)
		if observacaoform.is_valid():
			observacao=observacaoform.save(commit=False)
			observacaoform.save()
			return redirect(home_sistema)
	else:
		
		observacaoform = ObservacaoForm(instance=observacao)
	return render(request,'SistemaEscolar/editar_observacao.html', {'observacaoform': observacaoform})
			


  
@login_required(login_url='page_login')
def cadastrar_aluno(request):
	if request.method =='POST':
		
		alunoform=AlunoForm(request.POST, request.FILES)
		if alunoform.is_valid():
			aluno=alunoform.save(commit=False)
			alunoform.save()

			return redirect(cadastrar_endereco, id=aluno.id)
	else:
		alunoform = AlunoForm()
	return render(request,'SistemaEscolar/cadastrar_aluno.html', {'alunoform': alunoform})


@login_required(login_url='page_login')
def detalhes_aluno(request, id):
	aluno = get_object_or_404(Aluno, pk=id)	
	endereco = get_object_or_404(Endereco, pessoa_id=aluno.id)
	matricula = Matricula.objects.filter(aluno_id=aluno.id)

	objeto={
		'aluno':aluno,
		'endereco':endereco,
		'matricula':matricula,
	}
	
	return render(request, 'SistemaEscolar/detalhes_aluno.html' , objeto)

 


@login_required(login_url='page_logino')
def cadastrar_endereco(request,id):
	aluno = get_object_or_404(Aluno, pk=id)

	if request.method=='POST':
		enderecoform=EnderecoForm(request.POST, request.FILES)
		if enderecoform.is_valid():
			endereco = enderecoform.save(commit=False)
		
			endereco.save()
			return render(request, 'SistemaEscolar/home_sistema.html', {'aluno': aluno})#direcionar para tela inicial

	else:
		enderecoform= EnderecoForm()
	return render(request, 'SistemaEscolar/cadastrar_endereco.html',{'enderecoform': enderecoform, 'aluno': aluno})		




@login_required(login_url='page_login')
def listar_alunos(request):
	alunos = Aluno.objects.all()
	matricula = Matricula.objects.all()

	return render(request, 'SistemaEscolar/listar_alunos.html', {'alunos':alunos, 'matricula':matricula})


@login_required(login_url='lpage_login')
def	listar_endereco(request):
	enderecos = Endereco.objects.all()
	return render(request, 'SistemaEscolar/listar_endereco.html', {'enderecos':enderecos})


@login_required(login_url='page_login')
def listar_turma(request):
	trumas = Turma.objects.all()
	return render(request, 'SistemaEscolar/listar_turma.html', {'turmas':turmas})


@login_required(login_url='page_login')
def listar_turno(request):
	turnos = Turno.objects.all()
	return render(request, 'SistemaEscolar/listar_turno.html', {'turnos':turnos})


@login_required(login_url='page_login')
def listar_matricula(request):
	matricula = Matricula.objects.all()
	return render(request, 'SistemaEscolar/listar_matricula.html',{'matricula':matricula})


@login_required(login_url='page_login')
def buscar_matricula(request,id):
	matricula= Matricula.objects.filter(aluno_id=id)
	#print(matricula.aluno_id)
	return render(request, 'SistemaEscolar/listar_matricula.html',{'matricula': matricula})



@login_required(login_url='page_login')
def listar_funcionario(request):
	funcionarios = Funcionario.objects.all()
	return render(request, 'SistemaEscolar/listar_funcionario.html', {'funcionarios': funcionarios})



@login_required(login_url='page_login')
def cadastrar_funcionario(request):
	if request.method =='POST':
		enderecoform=EnderecoForm(request.POST, request.FILES)
		funcionarioform=FuncionarioForm(request.POST, request.FILES)
		if enderecoform.is_valid() and funcionarioform.is_valid():
			funcionario=funcionarioform.save(commit=False)
			
			funcionarioform.save()

			endereco=enderecoform.save(commit=False)
			endereco.funcionario_id=funcionario.id
			enderecoform.save()
			
			
			return redirect(cadastrar_endereco, id=funcionario.id)
	else:
		enderecoform = EnderecoForm()
		funcionarioform = FuncionarioForm()
	return render(request,'SistemaEscolar/cadastrar_funcionario.html', {'enderecoform': enderecoform, 'funcionarioform': funcionarioform})



@login_required(login_url='page_login')
def cadastrar_matricula(request):
	if request.method =='POST':
		
		matriculaform=MatriculaForm(request.POST, request.FILES)

		if matriculaform.is_valid():

			matricula=matriculaform.save(commit=False)			
			matriculaform.save()						
			return redirect(listar_alunos)


	else:
		
		matriculaform = MatriculaForm()
	return render(request,'SistemaEscolar/cadastrar_matricula.html', {'matriculaform': matriculaform})






