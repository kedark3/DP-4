# Approach: Iterative. Every time we encounter "1" at i,j, we look at (i+1,j+1) diagonally and if it is also "1"
# then we try to look at the row and column (i+1,i) and (j+1,j) and if it is a square, we increment k by 1
# else we set flag to false and break out of the loop. Ans will be max of ans and k at the end of each iteration
# and final answer is `ans*ans` cause we need to calculate total area of the square.
# TC: O(m^2 * n^2)
# SC: O(1)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    k = 1
                    flag = True
                    while (i+k) < m and (j+k) < n and flag:
                        # check row
                        for x in range(i+k, i-1, -1):
                            if matrix[x][j+k] == "0":
                                flag = False
                                break
                        # check column
                        for x in range(j+k, j-1, -1):
                            if matrix[i+k][x] == "0":
                                flag = False
                                break
                        if flag:
                            k += 1
                    ans = max(ans,k)
        return ans*ans
                                