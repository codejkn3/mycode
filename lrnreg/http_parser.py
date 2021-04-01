#!/usr/bin/env python3

# Do imports

import urllib.request
import re

url = ""

print("Where should we search?")
url = input()

while url.lower() != 'quit':

    #get url

    print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")

    #get what to search for
    searchFor = input()

    #parse the URL
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    #now check for a match
    #if re.search(searchFor, searchMe):
    numResults = len(re.findall(searchFor, searchMe))
    if numResults > 0:
        print(f"Found {numResults} matches!")
    else:
        print("No match!")

    url = input("\nEnter another url or quit so stop\n")
