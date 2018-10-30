import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDRjavHrEvei0wuHLRYUEbEtRH3YMGcKpQ')
place_types =  ['hospital','bank','book_store','bus_station','school','train_station','restaurant','gym','gas_station','doctor','electronics_store','pharmacy',]#'beauty_salon','cafe','car_repair','church','clothing_store','dentist','hindu_temple','mosque','movie_theater','subway_station','supermarket','atm','bakery']

def get_latitude_and_longitude(address):
	geocode_result = gmaps.geocode(address)
	location = geocode_result[0]['geometry']['location']
	print(location)
	return location

def get_closest_places(location,place_type,num=2,radius=600):
	l = []
	places_result=gmaps.places_nearby(location=(location['lat'], location['lng']),type=place_type,radius=radius)['results']
	for i in range(min(num,len(places_result))):
		l.append((places_result[i]['name'], places_result[i]['geometry']['location']))
	return l

def get_distance_and_time(origin,destination):
	t = gmaps.distance_matrix([origin],[destination],mode='driving')['rows'][0]['elements'][0]
	return t['distance']['text'], t['duration']['text']

#for testing
if __name__ == '__main__':
	a = get_latitude_and_longitude('Wind Tunnel Road, Bangalore 560017')
	b = get_closest_places(a,'atm',radius=1000)
	c = get_distance_and_time(b[0][1],b[1][1])
	print(a)
	print(b)
	print(c)