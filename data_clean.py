import re

number = r'\d+(,\d{3})*\.*\d*'


def clean_tags(soup):
    for tag in soup.find_all(['sup', 'span']):
        tag.decompose()


def remove_parentheses(value):
    if isinstance(value, list):
        value_list = []
        for item in value:
            item = re.sub(r'\([^)]*\)', '', item)
            value_list.append(item)
        return value_list
    else:
        value = re.sub(r'\([^)]*\)', '', value)
        return value


def minute_to_integer(running_time):
    if running_time != 'N/A':
        if isinstance(running_time, list):
            return int(running_time[0].split(' ')[0])
        else:
            return int(running_time.split(' ')[0])
    else:
        return None


# CASES
# $12.2 million --> 12200000
# $789.000 --> 790000
def money_conversion(money):
    value_string = re.search(number, money).group()
    value = float(value_string.replace(',', ''))
    return value


print(money_conversion('$790,000.25'))
