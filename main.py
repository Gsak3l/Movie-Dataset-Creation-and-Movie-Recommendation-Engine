import json
from get_disney_films import scrape_disney_films

if __name__ == '__main__':
    print(json.dumps(scrape_disney_films(), indent=4))
    print(len(scrape_disney_films()))
