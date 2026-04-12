def non_rep_char(str):
    freq = {}
    for char in str:
        # if char in freq:  # 
        print(freq)
        freq[char] = freq.get(char,0) + 1
        #     freq[char] += 1
        # else:
        #     freq[char] = 1
    print(freq)
    for char in str:
        if freq[char] == 1:
            print(f"non repeating char is {char}")
            return
str = input("enter the sting : ")
non_rep_char(str.lower())
