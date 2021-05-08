import folium
import pandas as pd 
df = pd.read_csv("../Data/data_air/AB_data_clean.csv")

manual_colors = ['#636efa', '#ef553b', '#00cc96']


#creating to different marker groups, one for each time period
Entire = folium.FeatureGroup(name='<span style=\\"color: manual_colors[0];\\">Entire home/apt</span>')
Private = folium.FeatureGroup(name='<span style=\\"color: manual_colors[1];\\">Private Room</span>')
Shared = folium.FeatureGroup(name='<span style=\\"color: manual_colors[2];\\">Shared Room</span>')

NYC_coor = (40.730610, -73.935242)

def add_marker_Entire(x):
      folium.CircleMarker(location=[x.latitude, x.longitude], radius= 0.5, color=manual_colors[0], weight = 2,  fill_color=manual_colors[0], fill=True, fill_opacity=1).add_to(Entire)

def add_marker_Private(x):
      folium.CircleMarker(location=[x.latitude, x.longitude], radius= 0.5, color=manual_colors[1], weight = 2,  fill_color=manual_colors[1], fill=True, fill_opacity=1).add_to(Private)

def add_marker_Shared(x):
      folium.CircleMarker(location=[x.latitude, x.longitude], radius= 0.5, color=manual_colors[2], weight = 2,  fill_color=manual_colors[2], fill=True, fill_opacity=1).add_to(Shared)


NY_map = folium.Map(NYC_coor, zoom_start=11, tiles = 'cartodbpositron')
folium.TileLayer('cartodbpositron').add_to(NY_map)

#apply the function we just created to every row in the dataframe
df[df.room_type == 'Entire home/apt'].apply(lambda x:  add_marker_Entire(x), axis =1)
df[df.room_type == 'Private room'].apply(lambda x:  add_marker_Private(x), axis =1)
df[df.room_type == 'Shared room'].apply(lambda x:  add_marker_Shared(x), axis =1)
#add borh marker groups to the map
Entire.add_to(NY_map)
Private.add_to(NY_map)
Shared.add_to(NY_map)
folium.map.LayerControl('topright', collapsed=False).add_to(NY_map)
#display map
NY_map.save('Map_room_type.html')