def reverse_segment(N,L,R):
    arr = list(range(1, N+1))
    while L < R:
        arr[L],arr[R] = arr[R],arr[L]
        L += 1
        R -= 1
    return "".join(map(str,arr))
print(reverse_segment(5,2,3))