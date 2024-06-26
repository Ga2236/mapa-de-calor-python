import pandas as pd
df= pd.read_csv('C:/Users/gabriel.marciano/Downloads/dadosabertos_poa_br/cat_acidentes.csv' , sep = ';')


import folium
from folium.plugins import HeatMap
mapa = folium.Map(location=[-30.1, -51.15], zoom_start=11)
coodenadas = list(zip(df.latitude, df.longitude))
mapa_calor = HeatMap(coodenadas,radius=9, blur=10)
mapa.add_child(mapa_calor)
#exiba o mapa
mapa