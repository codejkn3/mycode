#!/usr/bin/env python3
'''
API script by John Nealy
'''

# imports always go at the top of your code
import requests


ZIPAPI = "http://api.zippopotam.us/US/"

def main():
    """Run time code"""
    # create r, which is our request object
    #r = requests.get("https://cat-fact.herokuapp.com/facts")
    #r = requests.get("https://restcountries.eu/rest/v2/all")
    city = input("Enter the full name of the city: ")
    state = input("Enter the 2-letter abbreviation for the state (e.g. FL) : ")
    zipsearch = ZIPAPI + state +"/" + city
    r = requests.get(zipsearch)

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    # print the City, state
    
    if r.status_code == 200:
        print(f"API is calling {r.url}\n")
        print(f" ZIP codes for {r.json().get('place name')}, {r.json().get('state abbreviation')}")

        #print zipcodes
        for places in r.json().get("places") :
            print(places.get("post code"),end=",")

main()

