import googlemaps

def address_checker(address):
	gmaps = googlemaps.Client(key='AIzaSyDeqniyBHyf4XdEwOBAtvtI8xPWnvQE5pk')
	#address = input("Enter the address you want to check: ")
	geocode_result = gmaps.geocode(address)
	if geocode_result != '[]':
	    return 'available'
	else:
	    return 'not available'
print(address_checker("princess hotel"))
