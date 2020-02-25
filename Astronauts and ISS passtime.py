# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:57:33 2020

@author: juanv
"""

# In this simple Python script I used the open-notify API
# to create a simple program that can tell us the names of 
# the astronauts in Space at the current time, and how long
# until the International Space Station is over the user´s location.

import json
import requests
import geocoder #geocoder is used to import the user´s location

#Defining a function to return the names of the astronauts in Space at the moment
def get_astro():
    response = requests.get("http://api.open-notify.org/astros.json")
    astronauts = json.loads(response.content)
    name_list = astronauts["people"]
    names = []
    for people in name_list:
     names.append(people["name"])
    return names

#Defining a function to return (in seconds) the time until the ISS is over the user´s location
def get_time(lat,lon): # Accepts two parameters: latitude, and longitude
    params = {"lat":lat,"lon":lon,"n":1}
    response = requests.get("http://api.open-notify.org/iss-pass.json?", params=params)
    response_dic = json.loads(response.content)
    time = response_dic["response"][0]["duration"]
    return time


var = input("\n\nWhat would you like to know?\n\n1-Which astronauts are in space right now \n2-When will the ISS pass over my location\n\n")

if var==str(1):
    astronauts = get_astro()
    print("\n\nThe following astronauts are in space: \n"+ str(astronauts))

if var==str(2):
    latlon = geocoder.ip('me').latlng #Using the geocoder module to get user´s location
    time = get_time(lat=latlon[0],lon=latlon[1])
    print("\nThe iss will take "+str(time)+" seconds to be over your location")
    


    
    

    

