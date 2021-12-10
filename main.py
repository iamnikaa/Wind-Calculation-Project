"""Main program for finding distance of any city from shoreline in Great Britain"""

import json
from fetch_sea_distance import fetchdistance


# DISTANCE = fetchdistance('London', 'Manchester').text     #request distance data from rapidapi
# write_obj = json.loads(DISTANCE)  #Deserialize the json object to prettify

# with open('distance_response.json', 'w') as dist_resp:    
#     json.dump(write_obj, dist_resp, indent = 4, sort_keys = True) #write the response data to distance_response.json file as prettified object

with open('distance_response.json', 'r') as dist_resp:
    from_record_dist_resp = json.load(dist_resp)

print(json.dumps(from_record_dist_resp['steps'], indent = 4))   #Display steps key from response