import json
import pickle
from get_disney_films import scrape_disney_films
from data import save_data, load_data
from data_clean import minute_to_integer
from money_conversion import convert_money
from date_conversion import convert_date


def load_json_data():
    movie_info_list_ = load_data('disney_data_cleaned.json')
    return movie_info_list_


def create_json_data():
    movie_info_list_ = scrape_disney_films()
    for movie in movie_info_list_:  # new fields
        movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))  # string to int
        movie['Budget (float)'] = convert_money(movie.get('Budget', 'N/A'))  # string to float
        movie['Box office (float)'] = convert_money(movie.get('Box office', 'N/A'))  # string to float
        movie['Release date (datetime)'] = convert_date(movie.get('Release date', 'N/A'))  # string to datetime
    save_data_pickle('disney_movie_data_cleaned_more.pickle', movie_info_list_)
    # save_data('disney_data_cleaned.json', movie_info_list_)
    # return movie_info_list_


def save_data_pickle(name, data):
    with open(name, 'wb') as f:
        pickle.dump(data, f)


def load_data_pickle(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    # movie_info_list = create_json_data()
    # create_json_data()
    movie_info_list = load_data_pickle('disney_movie_data_cleaned_more.pickle')
    print(movie_info_list)
