n = [5,9,6,2,8,1]
for i in range(len(n)-1):
    for j in range(len(n)-i-1):
        print(f"- {len(n)-i-1}")
        if n[j] > n[j+1]:
            n[j],n[j+1] = n[j+1],n[j]
print(n)