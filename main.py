import json
import requests
import urllib

from pprint import pprint
from data import save_data, load_data, save_json_data, load_json_data, save_data_pickle, load_data_pickle

if __name__ == '__main__':
    # save_data_pickle('disney_movie_data_cleaned_with_scores.pickle')
    print(load_data_pickle('disney_movie_data_cleaned_with_scores.pickle')[-59])
