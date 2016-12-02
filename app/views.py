from django.shortcuts import render
from django.http import HttpResponse
from  formularios import busca
from plotMap import plotMap
# Create your views here.

def index(request):
	nome_arquivo=''
	if request.method == "GET" and request.GET.__contains__('busca'):
		busca_str = request.GET['busca']
		p = plotMap()
		if busca_str == '':
			busca_str = '*'
		nome_arquivo = p.plot(busca_str)
	form_busca = busca()
	return render(request, "index.html", {'form':form_busca.as_table(), 'arquivo':nome_arquivo})
