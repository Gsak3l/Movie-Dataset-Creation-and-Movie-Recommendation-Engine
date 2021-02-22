import json
from get_disney_films import scrape_disney_films
from data import save_data, load_data
from data_clean import minute_to_integer
from conversion import money_conversion

if __name__ == '__main__':
    movie_info_list = scrape_disney_films()
    # movie_info_list = load_data('disney_data_cleaned.json')

    for movie in movie_info_list:  # new fields
        movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))  # string to int
        movie['Budget (float)'] = money_conversion(movie.get('Budget', 'N/A'))  # string to float
        movie['Box office (float)'] = money_conversion(movie.get('Box office', 'N/A'))  # string to float

    save_data('disney_data_cleaned.json', movie_info_list)
    print(json.dumps(movie_info_list, indent=4), len(movie_info_list))
