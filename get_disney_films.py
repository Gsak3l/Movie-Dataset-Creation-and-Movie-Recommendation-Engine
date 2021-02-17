import requests
from bs4 import BeautifulSoup as bs
from get_info_box import scrape_info_box


def scrape_disney_films():
    movie_info_list = []
    base_path = 'https://en.wikipedia.org'

    r = requests.get('https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films')
    soup = bs(r.content, features='html.parser')

    movies = soup.select('.wikitable.sortable i a')
    for index, movie in enumerate(movies):
        try:
            relative_path = movie['href']
            title = movie['title']
            movie_info_list.append(scrape_info_box(base_path + relative_path))
        except Exception as e:
            print(movie.get_text())
            print(e)

    return movie_info_list
