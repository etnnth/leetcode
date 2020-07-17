class Solution:
    def maxUncrossedLines(self, A, B):
        A = [a for a in A if a in B]
        B = [b for b in B if b in A]
        m, n = len(A), len(B)
        if n>m:
            m,n=n,m
            A,B=B,A
        dp = [0] * (n + 1)
        for a in A:
            for j in range(n-1,-1,-1):
                if a == B[j]: dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j:j+2])
        return dp[n]
