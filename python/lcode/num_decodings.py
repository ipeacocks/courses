def numDecodings(s): 
    if not s:
        return 0

    dp = [0 for x in range(len(s) + 1)] 
    print(dp)
    # base case initialization
    dp[0] = 1
    if s[0] == "0":
        return 0
    else:
        dp[1] = 1

    for i in range(2, len(s) + 1): 
        # One step jump
        if 0 < int(s[i-1:i]):
            dp[i] += dp[i - 1]
        # Two step jump
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]
    # return dp[len(s)], dp
    return dp

print(numDecodings("4567112"))

# 11,1,1,1
# 1,11,1,1
# 1,1,11,1
# 1,1,1,11
# 11,11,1
# 1,11,11
# 11,1,11
# 1,1,1,1,1

# 4,5,6,7,1,1,2
# 4,5,6,7,11,2
# 2,5,6,7,1,12

