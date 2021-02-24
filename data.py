import json
import pickle


from data_clean import minute_to_integer
from date_conversion import convert_date
from get_disney_films import scrape_disney_films
from money_conversion import convert_money


def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data(title):
    with open(title, encoding='utf-8') as f:
        return json.load(f)


def save_json_data():
    movie_info_list_ = scrape_disney_films()
    for movie in movie_info_list_:  # new fields
        movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))  # string to int
        movie['Budget (float)'] = convert_money(movie.get('Budget', 'N/A'))  # string to float
        movie['Box office (float)'] = convert_money(movie.get('Box office', 'N/A'))  # string to float
        movie['Release date (datetime)'] = str(convert_date(movie.get('Release date', 'N/A')))  # string
    save_data('disney_data_cleaned.json', movie_info_list_)


def load_json_data():
    movie_info_list_ = load_data('disney_data_cleaned.json')
    return movie_info_list_


def save_data_pickle(name, data):
    movie_info_list_ = scrape_disney_films()
    for movie in movie_info_list_:  # new fields
        movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))  # string to int
        movie['Budget (float)'] = convert_money(movie.get('Budget', 'N/A'))  # string to float
        movie['Box office (float)'] = convert_money(movie.get('Box office', 'N/A'))  # string to float
        movie['Release date (datetime)'] = convert_date(movie.get('Release date', 'N/A'))  # string to datetime

    with open(name, 'wb') as f:
        pickle.dump(data, f)


def load_data_pickle(name):
    with open(name, 'rb') as f:
        return pickle.load(f)
