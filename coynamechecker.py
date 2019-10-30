"""
Created by Bilesanmi Faruk
"""
# importing required modules 
import requests, json 
  
# enter your api key here 
api_key = 'AIzaSyDeqniyBHyf4XdEwOBAtvtI8xPWnvQE5pk'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

name = input("Enter the name if the company: ")
address = input("Enter the address of the company:  ")

query = name

r = requests.get(url + 'query=' + query + '&key=' + api_key)
#  json format data into python format data 
x = r.json() 
y = x['results']

try:
    # keep looping upto lenght of y 
    for i in range(len(y)): 
        # Print name and address of the query and coy_address == address:
        coy_name = y[i]['name']
        coy_address = y[i]['formatted_address']
        print(coy_name)
        print(coy_address) 
    if name.lower() in coy_name.lower():
        print('the name is there')
        print("Both names correlate, It is probably legit")
    else:
        print("It's probably fake")
except NameError:
    print("It's probably fake")
    
