import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDeqniyBHyf4XdEwOBAtvtI8xPWnvQE5pk')
address = input("Enter the address you want to check: ")
geocode_result = gmaps.geocode(address)
if geocode_result != '[]':
    print('available')
else:
    print('not available')
