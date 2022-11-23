def rob(nums):
    dp = [0] * (len(nums)-1)
    if len(nums) > 2:
        dp1 = [0] * (len(nums) - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        nums1 = nums[1:]
        dp1[0] = nums1[0]
        dp1[1] = max(nums1[1], nums1[0])
        for j in range(2, len(nums1)):
            dp1[j] = max(dp1[j - 1], dp1[j - 2] + nums1[j])
        return max(dp[-1], dp1[-1])
    return max(nums)


print(rob([1,3,1,3,100]))
