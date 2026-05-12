def max_words(sentences):
    max_count = 0
    for sentence in sentences:
        space_count = 0
        for ch in sentence:
            if ch == " ":
                space_count += 1
            words = space_count + 1
        if words > max_count:
            max_count = words
    print(f"maximum word count is : {max_count}")
sentences = ["please wait", "continue to talk", "continue to win"]
max_words(sentences)