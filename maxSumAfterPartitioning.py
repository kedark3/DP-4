# Approach: Dp approach 
# Subproblem: At each index, starting from 0, what is the maximum number we have there and what's the max amount we can make with that. And then, we expand it to `k` elements in backwards manner
# Algorithm:
# 1. initalize DP arr of size same as input arr and dp[0]=arr[0]
# 2. Iterate over input arr and consider current element as current max element and partition of size 1
# 3. checking i-j+1(partition size) before doing step 4, to ensure not go out of bounds on left end of the input array
# 4. Make current_max either: 
#   a. as partition_size * max + dp[last element before partition start]
#   b. Or just partition_size * max  if i-j is going negative as we are still in the beginning of array and we can't expand till partition of size k elements
# 5. Update dp[i] with curr_max if it is greater
# 6. In the end, return last element in the dp array
# TC: O(nk)
# SC: O(n)
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # DP array of size 
        dp = [0] * (len(arr))
        dp[0] = arr[0]
        
        # start from index 1 of arr
        for i in range(1, len(arr)):
            maxi = arr[i]
            # [1,15,7,9,2,5,10]
            for j in range(1,k+1):
                # find max in current elements
                maxi = max(maxi, arr[i-j+1])
                if i-j+1 >= 0:  # to check if it is a valid
                    # multiply that with size of partition i-j+1
                    if i-j >= 0:
                        curr = j*maxi + dp[i-j]
                    else:
                        curr = j*maxi
                # update dp with max for current index
                dp[i] = max(dp[i], curr)

        # return the last value in Dp
        return dp[-1]