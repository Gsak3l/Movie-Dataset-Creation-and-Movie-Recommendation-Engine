from datetime import datetime


def strip_parentheses(date):  # deleting parentheses
    return date.split('(')[0].strip()


def convert_date(date):
    if isinstance(date, list):  # checking if there are double or more dates
        date = date[0]

    date_str = strip_parentheses(date)
    print(date_str)

    fmts = ['%B %d, %Y', '%d %B %Y']  # month-day-year or date-month-year
    for fmt in fmts:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            pass
            return None
