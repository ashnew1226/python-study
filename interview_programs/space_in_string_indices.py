def space_in_string(sentence,spaces):
    result = ""
    j = 0
    for i in range(len(sentence)):
        if j < len(spaces) and i == spaces[j]:
            result += " "
            j += 1
        result += sentence[i]
    print(result)

sentence = "RajaSoftwareLabs"
spaces = [4, 12]
space_in_string(sentence,spaces)