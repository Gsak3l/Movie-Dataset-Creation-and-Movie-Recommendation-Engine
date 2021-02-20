import json
from get_disney_films import scrape_disney_films
from data import save_data, load_data
from data_clean import minute_to_integer

if __name__ == '__main__':
    # movie_info_list = scrape_disney_films()
    # waiting is so boring 😪
    movie_info_list = load_data('disney_data_cleaned.json')
    for movie in movie_info_list:  # new field with simply the integer for movie length
        movie['Running time (int)'] = minute_to_integer(movie.get('Running time', 'N/A'))
    save_data('disney_data_cleaned.json', movie_info_list)
    print(json.dumps(movie_info_list, indent=4), len(movie_info_list))
