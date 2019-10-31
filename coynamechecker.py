"""
Created by Bilesanmi Faruk
"""
# importing required modules 
import requests, json 
import time  
# enter your api key here 
def match_address_name(qname, address):
    #global coy_nameq 
    api_key = 'AIzaSyDeqniyBHyf4XdEwOBAtvtI8xPWnvQE5pk'

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    #name = input("Enter the name if the company: ")
    #address = input("Enter the address of the company:  ")

    query = qname

    r = requests.get(url + 'query=' + query + '&key=' + api_key)
    #  json format data into python format data 
    x = r.json() 
    y = x['results']
    time.sleep(5)
    #try:
        # keep looping upto lenght of y 
    for i in range(len(y)): 
        # Print name and address of the query and coy_address == address:
        print (y[i]['name'])



