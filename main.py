from bs4 import BeautifulSoup as bs
import requests


def get_info_box():
    r = requests.get('https://en.wikipedia.org/wiki/Toy_Story_3')
    soup = bs(r.content)
    # contents = soup.prettify()
    info_box_ = soup.find(class_='infobox vevent')
    # info_box_ = info_box_.prettify()
    info_rows = info_box_.find_all('tr')
    for row in info_rows:
        print(row.prettify())
    return ''


if __name__ == '__main__':
    info_box = get_info_box()
    print(info_box)
