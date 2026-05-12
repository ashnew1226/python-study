def decrypt_chars(s):
    n = len(s)
    odd_count = (n+1)//2
    odd_part = s[:odd_count]
    even_part = s[odd_count:]

    odd_part = odd_part[::-1]
    result = []
    i = j = 0
    for k in range(n):
        if k % 2 == 0:
            result.append(odd_part[i])
            i += 1
        else:
            result.append(even_part[j])
            j += 1
    print("".join(result))
decrypt_chars("rmgae") 