import folium 
import pandas
data=pandas.read_csv("volcanoes.txt")
map=folium.Map(location=[-80,100],zoom_start=6,tiles="Mapbox Bright")



lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])



def colorproduce(elevation):
  if elevation>2000:
    return 'orange'
  elif elevation<=2000:
    return 'blue'
	

fgv=folium.FeatureGroup(name="volcanoes")

	
	
for lt,ln,el in zip(lat,lon,elev):
  fgv.add_child(folium.CircleMarker(location=(lt,ln),radius=6,popup=str(el)+"m",fill_color=colorproduce(el),color='grey',fill=True,fill_opacity=0.7))
  
  
fgp=folium.FeatureGroup(name="population")

  
  
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),style_function=lambda x:{'fill_Color':'yellow' if x['properties']['P0P2005']<10000000
else 'orange' if 10000000<= x['properties']['P0P2005']<20000000 else 'red'}))


map.add_child(fgv);
map.add_child(fgp);
map.save("maps.html");

