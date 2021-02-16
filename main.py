import requests
import json
from bs4 import BeautifulSoup as bs
from scrape_info_box import get_info_box

if __name__ == '__main__':
    info_box = get_info_box()
    print(json.dumps(info_box, indent=4))  # json helps with the way I display things on print
