import requests
from bs4 import BeautifulSoup as bs
from data_clean import clean_tags, remove_parentheses


def scrape_info_box(url):
    movie_info = {}  # dictionary

    r = requests.get(url)
    soup = bs(r.content, features='html.parser')

    clean_tags(soup)

    # contents = soup.prettify()
    info_box_ = soup.find(class_='infobox vevent')
    # info_box_ = info_box_.prettify()
    info_rows = info_box_.find_all('tr')

    for index, row in enumerate(info_rows):
        if index == 0:  # title
            movie_info['title'] = row.find('th').get_text(' ', strip=True)
        else:
            header = row.find('th')
            if header:
                content_key = row.find('th').get_text(' ', strip=True)
                content_value = get_content_value(row.find('td'))
                # content_value = remove_parentheses(content_value)
                movie_info[content_key] = content_value

    return movie_info


def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(' ', strip=True).replace('\u00a0', ' ') for li in row_data.find_all('li')]
    elif row_data.find('br'):
        return [text for text in row_data.stripped_strings]
    else:
        return row_data.get_text(' ', strip=True).replace('\u00a0', ' ')
