a = [5,5,7,8,8,9,9,10,10]
uniq_array =  []

for i in a:
    if i not in uniq_array:
        uniq_array.append(i)
print(uniq_array)
uniq_array.append(5)
print(uniq_array)