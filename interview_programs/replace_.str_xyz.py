# with using split and join
# def replace_str(s):
#     words = s.split(".")
#     for i in range(len(words)):
#         if i % 2 == 1:
#             words[i] = "xyz"
#     return ".".join(words)
# print(replace_str("i.like.this.program.very.much"))


# without using inbuilt method

def replace_str(s):
    result = ""
    word = ""
    word_count = 1
    for char in s:
        print(f"------- {char}")
        if char != ".":
            word += char
        else:
            print(f"inside else {char}")
            if word_count % 2 == 0:
                result += "xyz"
            else:
                result += word
            result += "."  #add . back
            word = ""
            print(f"word---{word}")
            word_count += 1
    if word:
        if word_count % 2 == 0:
            result += "xyz"
        else:
            result += word
    return result
print(replace_str("i.like.this.program.very.much"))