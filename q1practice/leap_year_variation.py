def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
def next_leap(year,n):
    result = []
    year += 1
    year += (4-year%4)%4   # math technicto find out which next year needed to directly divisible by four
    while len(result) < n:
        if is_leap(year):
            result.append(str(year))
        year += 4
    print(",".join(result))
next_leap(997,4)