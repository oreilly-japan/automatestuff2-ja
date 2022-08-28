# 演習プロジェクト 7.18.1 

import re

def detect_date(s):
    date_regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    for day, month, year in date_regex.findall(s):
        day = int(day)
        month = int(month)
        year = int(year)

        if year < 1000 or year > 2999:
            print(f'不正な年です {year}')
            return None

        if month < 1 or month > 12:
            print(f'不正な月です {month}')
            return None

        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                max_day = 29
            else:
                max_day = 28
        elif month in (4, 6, 9, 11):
            max_day = 30
        else:
            max_day = 31
        if day < 1 or day > max_day:
            print(f'不正な日です {day}')
            return None
        return day, month, year
    return None

if __name__ == '__main__':
    assert detect_date('Today is 15/08/1945.') == (15, 8, 1945)
    assert detect_date('There is no 31/02/2020.') == None
    assert detect_date('There is no 31/04/2021.') == None
    assert detect_date('There is no 15/00/1945.') == None
    assert detect_date('There is no 15/13/1945.') == None
    assert detect_date('There is no 00/08/1945.') == None
    assert detect_date('There is no 32/18/1945.') == None
    assert detect_date('There is no 01/08/9999.') == None
    assert detect_date('Bad format: 1945/08/15.') == None

