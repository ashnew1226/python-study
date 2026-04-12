def is_anagram(a, b):
    if len(a) != len(b):
        return False
    freq = {}
    for char in a:
        freq[char] = freq.get(char,0)+1
    for char in b:
        if char not in b:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    return True
print(is_anagram("act","tac"))