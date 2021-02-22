import re

amounts = r'thousand|million|billion'
number = r'\d+(,\d{3})*\.*\d*'

word_re = rf'\${number}\s({amounts})'
value_re = rf'\${number}'

'''
CASES
$12.2 million --> 12200000
$789.000 --> 790000
'''


def parse_value_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(',', ''))
    return value


def parse_word_syntax(string):
    pass


def money_conversion(money):
    word_syntax = re.search(word_re, money)
    value_syntax = re.search(value_re, money)

    if word_syntax:
        return None
    elif value_syntax:
        return parse_value_syntax(value_syntax.group())


print(money_conversion('$12.2 billion'))
# print(re.search(word_re, '$12.2 million').group())
