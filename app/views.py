from django.shortcuts import render
from django.http import HttpResponse
from  formularios import busca
from plotMap import redisInterface, plotMap
# Create your views here.

def index(request):
	if request.method == "GET":
		busca_str = request.GET['busca']
		p = plotMap()
		nome_arquivo = p.plot(busca_str)
	form_busca = busca()
	return render(request, "index.html", {'form':form_busca.as_table()})
