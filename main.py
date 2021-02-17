import requests
import json
from bs4 import BeautifulSoup as bs
from scrape_info_box import get_info_box


def scrape_disney_films():
    r = requests.get('https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films')
    soup = bs(r.content, features='html.parser')
    contents = soup.prettify()
    # print(contents)
    # movies = soup.findAll(class_='wikitable sortable')
    movies = soup.select('.wikitable.sortable i')
    for index, movie in enumerate(movies):
        try:
            relative_path = movie.a['href']
            title = movie.a['title']
            print(relative_path, title)
        except Exception as e:
            print(movie.get_text())
            print(e)


if __name__ == '__main__':
    # info_box = get_info_box()
    # print(json.dumps(info_box, indent=4))  # json helps with the way I display things on print
    scrape_disney_films()
