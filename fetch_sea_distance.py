"""Module to fetch upwind distance to shoreline for a given location
(uses rapidapi 'Distance' api - https://rapidapi.com/Distance.to/api/distance/)"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()   #initialize local environment variable (.env) file

def fetchdistance(fromloc, toloc):
    """Function to fetch distance between two cities in Great Britain.
    Input parameters: fromloc = From location, toloc = To location"""

    from_loc_str = '\"' + fromloc + '\"'
    to_loc_str = '\"' + toloc + '\"'

    url = "https://distanceto.p.rapidapi.com/get"

    querystring = {"route":"[{\"t\":" + from_loc_str + ",\"c\":\"GB\"},{\"t\":"+\
                to_loc_str + ",\"c\":\"GB\"}]", "car":"false", "foot":"false"}

    apikey = os.environ['apikey']   #fetch apikey from local environment variables '.env' file

    headers = {
        'x-rapidapi-host': "distanceto.p.rapidapi.com",
        'x-rapidapi-key': apikey
        }

    response = requests.get(url, headers=headers, params=querystring)
    return response
    