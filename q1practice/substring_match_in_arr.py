def is_substring(small,big):
    if (len(small) > len(big)):
        return False
    for i in range(len(big)-len(small)+1):
        match = True
        for j in range(len(small)):
            if big[i + j] != small[j]:
                match = False
                break
        if match:
            return True
    return False
def substr_match(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                if is_substring(words[i],words[j]):
                    result.append(words[i])
                    break
    return result
words = ["mass","as","hero","superhero"]
print(substr_match(words))