def max_odd(s):
    ones = ''
    zeros = ''
    for n in s:
        if n == '1':
            ones += '1'
        elif n == '0':
            zeros += '0'
    return ones[:-1] + zeros + '1'
print(max_odd('01010110'))