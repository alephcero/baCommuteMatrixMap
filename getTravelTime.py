#libraries
def getTravelTime(origins,destinations,preferences = 'fewer_transfers'):
    '''
    This function takes a coordinates tuple for origin
    a coordinates tuple for destination
    and returns the travel time in seconds
    preference could be fewer_transfers or less_walking
    '''
    key = os.getenv('GOOGLEAPIDISTANCE')
    gmaps = googlemaps.Client(key=os.getenv('GOOGLEAPIDISTANCE'))
    travel = gmaps.distance_matrix(origins = origins,destinations = destinations, mode="transit", traffic_model="best_guess", transit_routing_preference = preferences)
    return travel['rows'][0]['elements'][0]['duration']['value']

