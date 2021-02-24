import json
import requests
import urllib

from pprint import pprint
from data import save_data, load_data, save_json_data, load_json_data, save_data_pickle, load_data_pickle


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


if __name__ == '__main__':
    movie_info_list = load_data_pickle('disney_movie_data_cleaned_more.pickle')
    # print(json.dumps(get_omdb_info('into the woods'), indent=4, sort_keys=True))
    info = get_omdb_info('Her')
    rotten = get_rotten_tomatoes_score(info)
    for movie in movie_info_list:
        title = movie['title']
        omdb_info = get_omdb_info(title)
        movie['imdb'] = omdb_info.get('imdbRating', None)
        movie['metascore'] = omdb_info.get('Metascore', None)
        movie['rotten_tomatoes'] = get_rotten_tomatoes_score(omdb_info)
    save_data_pickle()
