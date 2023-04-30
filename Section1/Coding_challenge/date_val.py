import re

date_pattern = re.compile(r"([0-2][0-9]|3[0-1])/(0[0-9]|1[0-2])/([0-2][0-9][0-9][0-9])")
dates = """
19/06/2041
27/09/2042
14/03/2043
08/12/2044
02/10/2045
31/02/2046
23/08/2047
06/05/2048
15/11/2049
01/02/2050
10/10/2051
25/07/2052
11/04/2053
28/12/2054
16/09/2055
31/02/2056
07/06/2057
19/01/2058
31/02/2020
31/02/2046
31/02/2056
31/02/2063
30/02/2022
08/12/2064
29/02/2023 (since 2023 is not a leap year)
32/04/2024
00/05/2025
13/13/2026
31/04/2028 (since April has only 30 days)
07/09/2100
"""
result = date_pattern.findall(dates)
Valid = []
Invalid = []
for day, month, year in result:
    day, month, year = int(day), int(month), int(year)
    date_list = [day, month, year]
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            Invalid.append(f"{day}/{month}/{year}")
        else:
            Valid.append(f"{day}/{month}/{year}")
    if month == 2:
        if day > 30:
            Invalid.append(f"{day}/{month}/{year}")
        else:
            Valid.append(f"{day}/{month}/{year}")
for dates in Valid:
    print(dates)
print()
for dates in Invalid:
    print(dates)
