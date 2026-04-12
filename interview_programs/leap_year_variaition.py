def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def next_leap_year(year, n):
    result = []
    year += 1
    while year % 4 != 0:
        year += 1
    while len(result) < n:
        if is_leap(year):
            result.append(year)
        year += 4
    print(", ".join(map(str, result)))

next_leap_year(999,1)