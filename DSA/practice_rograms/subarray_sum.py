# naive approch

a = [3,8,2,5,7,6,12]
n = len(a)
w = 4

maxx = float('-inf')
for i in range(n-w+1):
    print(f"--{i}")
    current = 0
    for j in range(i,(i+w)):
        current = current + a[j]
        if current > maxx:
            maxx = current
        else:
            maxx = maxx
print(maxx)

# sliding window approach
a = [3,8,2,5,7,6,12]
n = len(a)
w = 4
current = 0
for i in range(0,w):
    current = current + a[i]
maxx = current
for i in range(1,n-w+1):
    current = current - a[i-1] + a[i+w-1]

    if current > maxx:
        maxx = current 

print(maxx)