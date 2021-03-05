import urllib
import requests


def get_omdb_info(title):
    base_url = 'http://www.omdbapi.com/?'
    parameters = {'apikey': 'e5a099f9', 't': title}
    params_encoded = urllib.parse.urlencode(parameters)
    full_url = base_url + params_encoded
    return requests.get(full_url).json()


def get_rotten_tomatoes_score(omdb_info):
    ratings = omdb_info.get('Ratings', [])
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            return rating['Value']
    return None
