def not_palindrome(s):
    if len(s) == 1:
        return -1
    rev = s[::-1]
    if rev != s:
        return rev
    arr = list(s)
    arr[-1],arr[-2] = arr[-2],arr[-1]
    return "".join(arr)
print(not_palindrome("abba"))