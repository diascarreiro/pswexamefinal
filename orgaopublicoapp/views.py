from django.shortcuts import render
from django.http import HttpResponse
from .forms import orgaopublicoform
from .models import orgaopublico


# Create your views here.


def index(request):
    #return HttpResponse("<h1>Aqui é o index<h1>")
    return render(request, 'orgaospublicos/index.html')


def orgaospublicos(request):
    #return HttpResponse("<h1>Aqui é a área de Órgão Público<h1>")
    orgaospublicos = orgaopublico.objects.all()
    busca = request.GET.get('search')
    if busca:
    	orgaospublicos = orgaopublico.objects.filter(nome_orgaopublico__icontains =busca)
    return render(request, 'orgaospublicos/orgaospublicos.html', {'orgaospublicos':orgaospublicos})


def editar_orgaospublicos(request, id):
	orgao = get_object_or_404(editar_orgaospublicos, pk=id)
	form = orgaopublicoform (instance=orgao)
	if(request.method=="POST"):
		form=orgaopublicoform(request.POST, request.FILES, instance=orgao)

		if form.is_valid():
			form.save()
			return redirect('orgaospublicos')

		else:

			return render(request, "orgaospublicos/editar_orgaospublicos.html",{'form':form, 'orgao':orgao})
	else:
		return render(request, "orgaospublicos/editar_orgaospublicos.html",{'form':form, 'orgao':orgao})


def criar_orgaospublicos (request):
    form = orgaopublicoform(request. POST)
    if request.method == "POST":
    	form = orgaopublicoform(request.POST, request.FILES)
    	if form.is_valid():
    		orgao = form.save()
    		orgao.save()
    		form = orgaopublicoform()
    return render(request, 'orgaospublicos/criar_orgaospublicos.html',{'form':form})


def deletar_orgaospublicos(request, id):
    orgao = get_object_or_404(orgaospublicos, pk=id)
    if request.method == "POST":
    	orgao.delete()
    	return redirect('orgaospublicos')
    return render (request, "orgaospublicos/deletar_orgaospublicos.html", {'orgao':orgao})

