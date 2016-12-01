
import random
import json
import os
import folium
from folium import plugins
from folium import MarkerCluster
import redis

class redisInterface():

	def readRedis(self, busca):
		conn = redis.StrictRedis(host='localhost', port=6379, db=0) #cria nova conexao com o redis
		coord = []
		chaves = conn.keys(busca)
		for i in chaves:
			coord_unit = json.loads(conn.get(i))
			coord_unit.reverse()
			coord.append(coord_unit)
		return coord	





class plotMap():

	def makeName(self, name):
		return str(name.replace("/", "_").replace(".", "_").replace(",", "_").replace(" ", "_").replace("*", "_")+".html")
	
	def plot(self, consulta):
		inicio = [-23.497084, -46.8854171]
		red = redisInterface()
		data = red.readRedis(consulta) 
		mapa = folium.Map(location=inicio, zoom_start=12)
		cluster = MarkerCluster("cluster").add_to(mapa)		
		for i in data:
			folium.Marker(i).add_to(cluster)
		mapa.add_children(plugins.HeatMap(data))
		nome_arquivo = self.makeName(consulta)
		path_arquivo = os.path.join('plot', nome_arquivo)
		mapa.save(path_arquivo)
		return nome_arquivo		



p = plotMap()
p.plot('*se*')




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
