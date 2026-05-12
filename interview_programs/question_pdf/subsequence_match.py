def subsequence_match(a,b):
    n,m = len(a),len(b)
    dp = [0]*(m+1) # number of ways to match for b
    dp[0] = 1      # initialy blank as 1
    for i in range(n):
        for j in range(m-1,-1,-1):   # reverse loop to avoid dublicacy
            if a[i] == b[j]:    
                dp[j+1] += dp[j]     # matches patten till j + 1
                print(dp)
            if dp[j+1] >= 2:         # stops when macthes more than 2 and returns the result
                return "Yes"
    return "Yes" if dp[m] >= 2 else "No"
print(subsequence_match([1,2,1,2],[1,2]))
