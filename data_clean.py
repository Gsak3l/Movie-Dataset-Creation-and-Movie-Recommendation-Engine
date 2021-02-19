def clean_tags(soup):
    for tag in soup.find_all(['sup', 'span']):
        tag.decompose()
    print(soup)
    while True:
        continue
