"""
Created by Bilesanmi Faruk
"""
# importing required modules 
import requests, json 
  
# enter your api key here 
def match_address_name(qname, address):
    api_key = 'AIzaSyDeqniyBHyf4XdEwOBAtvtI8xPWnvQE5pk'

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    #name = input("Enter the name if the company: ")
    #address = input("Enter the address of the company:  ")

    query = qname

    r = requests.get(url + 'query=' + query + '&key=' + api_key)
    #  json format data into python format data 
    x = r.json() 
    y = x['results']
    coy_nameq = "ss"
    coy_address = "gg"
    try:
            # keep looping upto lenght of y 
        for i in range(len(y)): 
            # Print name and address of the query and coy_address == address:
            coy_nameq = y[i]['name'] 
            coy_address = y[i]['formatted_address'] 
            lola = coy_nameq
        if (qname.lower() in lola.lower()) and (address.lower() in coy_address.lower()):
            return "They correlate, It is probably legit"
        else:
            return "It's probably fake"
    except NameError:
        return "It's probably fake"
#print(match_address_name("appzone", "350 borno way"))  
