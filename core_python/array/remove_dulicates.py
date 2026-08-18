def duplicates(arr):
    seen = []
    duplicate = []
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.append(arr[i])
        else:
            duplicate.append(arr[i])
    # print(f"non duplicate : {seen}")
    print(f"duplicates : {duplicate}")
arr = [1,22,22,4,3,1]
duplicates(arr)