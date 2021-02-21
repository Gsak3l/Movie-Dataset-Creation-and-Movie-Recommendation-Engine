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


def parse_value_syndax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(',', ''))
    return value


def money_conversion(money):
    value_syntax = re.search(value_re, money).group()


print(re.search(word_re, '$12.2 million').group())

