# app to practice for loop

# import required libraries
import pandas
import folium

# read in the CSV data from Australia Post
town_data = pandas.read_csv('a-towns.csv')

# extract the latitude and longitude data from the CSV file,
# and assign them to variables, as lists
latitude = list(town_data.loc[:,'latitude'])
longitude = list(town_data.loc[:,'longitude'])
name = list(town_data.loc[:,'name'])
elevation = list(town_data.loc[:,'elevation'])

# Get the maximum and minimum elevations
# max_elev = max(elevation)
# print(max_elev)
# 
# min_elev = min(elevation)
# print(min_elev)

def fl_clr(elev):
    if elev <= 500:
        fill_color = 'green'
    elif elev <= 1000:
        fill_color = 'orange' 
    else:
        fill_color = 'red'
    
    return fill_color

# # a function to combine the latitude and longitude into a single list
# def combine_lat_long():
#     lat_long = []
#     for i in range(len(latitude)):
#         location = [latitude[i], longitude[i]]
#         lat_long.append(location)
#     return lat_long

# # the single list of latitude and longitude 
# lat_long = combine_lat_long()

# create the folium map
world_map = folium.Map(location=[-23.698331, 133.881289],
                        zoom_start=5,
                        tiles='Stamen Terrain')

# create a feature group for the towns marker layer
towns_fg = folium.FeatureGroup(name="Australian A Towns")

# create the towns marker layer,
# by iterating through the lat_long list, and names list for the popups
for lt,ln,nm, elev in zip(latitude, longitude, name, elevation):
    towns_fg.add_child(folium.CircleMarker(location=[lt,ln],
                                           radius=6,
                                           popup=str(nm) + ', Elevation:' + str(elev) + 'm',
                                           color='black',
                                           fill_color=fl_clr(elev)))

population_fg = folium.FeatureGroup(name="Country Populations")

population_fg.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig'),
                                  name = 'Populations',
                                  style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                              else 'red'}))

world_map.add_child(towns_fg)
world_map.add_child(population_fg)

world_map.add_child(folium.LayerControl(position = 'topleft', 
                                        collapsed = True,
                                        ))

world_map.save('towns_map.html')

