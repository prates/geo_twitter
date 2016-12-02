
import os
import time
import random
import json
import folium
from folium import plugins
from folium import MarkerCluster
import redis
import CONFIG

class RedisInterface():

	def read_redis(self, busca):
		conf = CONFIG.REDIS
		conn = redis.StrictRedis(host=conf['host'], port=conf['port'], db=conf['db']) #cria nova conexao com o redis
		coord = []
		chaves = conn.keys(busca)
		for i in chaves:
			coord_unit = json.loads(conn.get(i))
			coord_unit.reverse()
			coord.append(coord_unit)
		return coord	





class plotMap():

	def make_name(self, name):
		'''
		>>> p = plotMap()
		>>> p.makeName('*se*')
		'_se_.html' 
		'''
		return str(name.replace("/", "_").replace(".", "_").replace(",", "_").replace(" ", "_").replace("*", "_")+".html")
	
	def destino(self):
		path_atual = os.path.dirname(os.path.realpath(__file__))
		diretorio = os.path.join(path_atual, 'plot')
		return diretorio
	
		
	
	def plot(self, consulta):
		inicio = CONFIG.COORDENADASMAPA
		diretorio = self.destino()
		nome_arquivo = self.make_name(consulta)
		path_arquivo = os.path.join(diretorio, nome_arquivo)
		red = RedisInterface()
		data = red.read_redis(consulta) 
		mapa = folium.Map(location=inicio, zoom_start=12)
		cluster = MarkerCluster("cluster").add_to(mapa)		
		for i in data:
			folium.Marker(i).add_to(cluster)
		mapa.add_children(plugins.HeatMap(data))
		mapa.save(path_arquivo)
		return nome_arquivo		



if __name__ == "__main__":
	import doctest
	doctest.testmod()




'''
# Create a heatmap with the data.

r = random.Random()

inicio = [-23.497084, -46.8854171] 

def nova_coord(rand, coor):
	return [rand+i for i in coor]

data=[ nova_coord(r.gauss(0.2, 0.1), inicio)  for i in range(100) ]

#print data

heatmap_map = folium.Map(location=inicio, zoom_start=12)

cluster = MarkerCluster("cluster").add_to(heatmap_map)
for i in data:
	folium.Marker(i).add_to(cluster)


heatmap_map.add_children(plugins.HeatMap(data))
heatmap_map.save("heatmap.html")
'''
