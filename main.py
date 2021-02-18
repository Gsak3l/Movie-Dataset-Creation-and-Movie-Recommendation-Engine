import json
from get_disney_films import scrape_disney_films


def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data(title):
    with open(title, encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    movie_info_list = scrape_disney_films()
    print(json.dumps(movie_info_list, indent=4), len(movie_info_list))

    save_data("disney_data.json", movie_info_list)
