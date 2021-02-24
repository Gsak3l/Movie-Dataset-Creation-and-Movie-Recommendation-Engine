import json
import pickle

from data_clean import minute_to_integer
from date_conversion import convert_date
from get_disney_films import scrape_disney_films
from money_conversion import convert_money
from scores import get_omdb_info, get_rotten_tomatoes_score


def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data(title):
    with open(title, encoding='utf-8') as f:
        return json.load(f)


def save_json_data(name):
    movie_info_list = scrape_disney_films()
    for movie in movie_info_list:  # new fields
        movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))  # string to int
        movie['Budget (float)'] = convert_money(movie.get('Budget', 'N/A'))  # string to float
        movie['Box office (float)'] = convert_money(movie.get('Box office', 'N/A'))  # string to float
        movie['Release date (datetime)'] = str(convert_date(movie.get('Release date', 'N/A')))  # string
        # SCORES
        title = movie['title']
        omdb_info = get_omdb_info(title)
        movie['imdb'] = omdb_info.get('imdbRating', None)
        movie['metascore'] = omdb_info.get('Metascore', None)
        movie['rotten_tomatoes'] = get_rotten_tomatoes_score(omdb_info)

    save_data(name, movie_info_list)


def load_json_data(name):
    movie_info_list = load_data(name)
    return movie_info_list


def save_data_pickle(name):
    movie_info_list = scrape_disney_films()
    for movie in movie_info_list:  # new fields
        movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))  # string to int
        movie['Budget (float)'] = convert_money(movie.get('Budget', 'N/A'))  # string to float
        movie['Box office (float)'] = convert_money(movie.get('Box office', 'N/A'))  # string to float
        movie['Release date (datetime)'] = convert_date(movie.get('Release date', 'N/A'))  # string to datetime
        # SCORES
        title = movie['title']
        omdb_info = get_omdb_info(title)
        movie['imdb'] = omdb_info.get('imdbRating', None)
        movie['metascore'] = omdb_info.get('Metascore', None)
        movie['rotten_tomatoes'] = get_rotten_tomatoes_score(omdb_info)

    with open(name, 'wb') as f:
        pickle.dump(movie_info_list, f)


def load_data_pickle(name):
    with open(name, 'rb') as f:
        return pickle.load(f)
