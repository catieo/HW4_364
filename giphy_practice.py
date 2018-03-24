import requests
import json
from giphy_api_key import api_key

def get_gifs_from_giphy(search_string):
    """ Returns data from Giphy API with up to 5 gifs corresponding to the search input"""
    baseurl = "https://api.giphy.com/v1/gifs/search"
    url_params = {"api_key" : api_key, "q" : search_string, "limit" : 5}
    response = requests.get(baseurl, url_params)
    gif_dict = json.loads(response.text)['data']
    return gif_dict
    # TODO 364: This function should make a request to the Giphy API using the input search_string, and your api_key (imported at the top of this file)
    # Then the function should process the response in order to return a list of 5 gif dictionaries.
    # HINT: You'll want to use 3 parameters in the API request -- api_key, q, and limit. You may need to do a bit of nested data investigation and look for API documentation.
    # HINT 2: test out this function outside your Flask application, in a regular simple Python program, with a bunch of print statements and sample invocations, to make sure it works!

# results = get_gifs_from_giphy("drake")
# f = open("practice.txt", 'w')
# f.write(str(results))
# f.close()
get_gifs_from_giphy("drake")
