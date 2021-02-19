import json
from get_disney_films import scrape_disney_films
from data import save_data, load_data

if __name__ == '__main__':
    movie_info_list = scrape_disney_films()
    save_data('disney_data.json', movie_info_list)
    # waiting is so boring 😪
    # movie_info_list = load_data('disney_data.json')
    print(json.dumps(movie_info_list, indent=4), len(movie_info_list))