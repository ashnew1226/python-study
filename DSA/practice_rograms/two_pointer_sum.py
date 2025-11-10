a = [1,2,4,5,6,8,10,12]
left = 0
right = len(a)-1

while(left<right):
    current_sum = a[left] + a[right]
    if current_sum == 10:
        print(f"combination of numbes is : {a[left]} - {a[right]}")
        left += 1
        right -= 1
    elif (current_sum < 10):
        left += 1
    else:
        right -= 1

