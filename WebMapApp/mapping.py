# Mucking around with Folium

import folium

map_1 = folium.Map(location=[-27.440988, 153.022004],
                   zoom_start=12,
                   tiles='Stamen Terrain')

map_1.add_child(folium.Marker([-27.538482, 153.019902], 
                    popup="Home sweet home",
                    icon=folium.Icon(icon='home', color='green')))

folium.CircleMarker([-27.477337, 153.028423], 
                    popup="University",
                    radius=20,
                    color="white",
                    fill_color="black"
                    ).add_to(map_1)
                    
map_1.add_child(folium.ClickForMarker(popup="You made a marker you clever person"))

map_1.save("Map_1.html")

# a more organised way of setting this up is to create a feature group. 
# a feature group allows you to add more controls later on to specific parts of the map,
# as things get more complicated

map_2 = folium.Map(location=[-28.263088, 153.571857],
                   zoom_start=13,
                   tiles='Stamen Terrain')

fg = folium.FeatureGroup(name="The Map 2")

#Parents current house marker
fg.add_child(folium.Marker(location=[-28.263088, 153.571857],
                           popup="Home Sweet Parents Home",
                           icon=folium.Icon(icon='cloud')))

# Eviron Rd house marker
fg.add_child(folium.Marker(location=[-28.310889, 153.492019],
                           popup="Old Home Sweet Parents Home",
                           icon=folium.Icon(icon='heart', color='red')))

map_2.add_child(fg)
map_2.save('Map_2.html')






