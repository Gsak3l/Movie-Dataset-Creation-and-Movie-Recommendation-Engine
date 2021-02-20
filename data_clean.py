import re


def clean_tags(soup):
    for tag in soup.find_all(['sup', 'span']):
        tag.decompose()


# I should create it sooner or later
def remove_parentheses(value):
    value_list = []
    if isinstance(value, list):
        for item in value:
            item = re.sub(r'\([^)]*\)', '', item)
            value_list.append(item)
        return value_list
    else:
        value = re.sub(r'\([^)]*\)', '', value)
        return value
