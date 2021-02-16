import requests
import json
from bs4 import BeautifulSoup as bs


def get_info_box():
    r = requests.get('https://en.wikipedia.org/wiki/Toy_Story_3')
    soup = bs(r.content, features='html.parser')
    # contents = soup.prettify()
    info_box_ = soup.find(class_='infobox vevent')
    # info_box_ = info_box_.prettify()
    info_rows = info_box_.find_all('tr')
    movie_info = {}  # dictionary
    for index, row in enumerate(info_rows):
        if index == 0:  # title
            movie_info['title'] = row.find('th').get_text(' ', strip=True)
        elif index == 1:  # picture
            continue
        else:
            content_key = row.find('th').get_text(' ', strip=True)
            content_value = get_content_value(row.find('td'))
            movie_info[content_key] = content_value

    return movie_info


def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(' ', strip=True).replace('\u00a0', ' ') for li in row_data.find_all('li')]
    else:
        return row_data.get_text(' ', strip=True).replace('\u00a0', ' ')


if __name__ == '__main__':
    info_box = get_info_box()
    print(json.dumps(info_box, indent=4))  # json helps with the way I display things on print
