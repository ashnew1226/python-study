def strlen(string):
    current_count = 1
    max_count = 1
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            current_count += 1
        else:
            max_count = max(max_count,current_count)
            current_count = 1
    return max(max_count,current_count)
print(strlen("aabbccdddd"))