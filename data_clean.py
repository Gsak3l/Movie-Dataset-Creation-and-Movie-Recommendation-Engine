from bs4 import BeautifulSoup as bs


def clean_tags(soup):
    for tag in soup.find_all(['sup', 'span']):
        tag.decompose()
