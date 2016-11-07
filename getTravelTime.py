#libraries
import googlemaps
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


#There should be a key stored as and enviromental variable
key = os.getenv('GOOGLEAPIDISTANCE')
gmaps = googlemaps.Client(key=os.getenv('GOOGLEAPIDISTANCE'))

def getTravelTime(origins,destinations):
'''
This function takes a coordinates tuple for origin
a coordinates tuple for destination
and returns the travel time in seconds
'''
    travel = gmaps.distance_matrix(origins = home,
    	destinations = work,
    	mode="transit",
        traffic_model="best_guess")
    return travel['rows'][0]['elements'][0]['duration']['value']

