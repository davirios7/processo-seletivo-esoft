from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.forms import UploadForm
from home.models import Usuario

# todas as functions que vão chamar os arquivos das páginas

def editUsuario(request, pk):
  usuario = Usuario.objects.get(pk=pk)
  if request.POST:
    usuario.nome = request.POST.get('nome')
    usuario.sobrenome = request.POST.get('sobrenome')
    usuario.idade = request.POST.get('idade')
    usuario.data_de_nascimento = request.POST.get('data_de_nascimento')
    usuario.email = request.POST.get('email')
    usuario.apelido = request.POST.get('apelido')
    usuario.observacao = request.POST.get('observacao')
    usuario.save()
    messages.success(request, 'Usuário editado com sucesso!!')
    return redirect(tabelaUsuarios)
  return render(request, 'editarUsuario.html', {'usuario': usuario})

def tabelaUsuarios(request):
  form = UploadForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect(tabelaUsuarios)
  dados = Usuario.objects.all().order_by('nome', 'sobrenome')
  return render(request, "tabelaUsuarios.html", {'dados': dados})

def principal(request):
  if request.POST:
    form = UploadForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(tabelaUsuarios)
    else:
      return HttpResponse('Error!!')
  return render(request, "principal.html", {'form': UploadForm})
