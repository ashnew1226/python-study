def mini_len(s):
    i = 0
    j = len(s)-1
    while i < j and s[i] == s[j]:
        char = s[i]
        while i <= j and s[i] == char:
            i += 1
        while i <= j and s[j] == char:
            j -= 1
    return j-i+1
print(mini_len('aabccabba'))