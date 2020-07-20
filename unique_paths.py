from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = (n - 1) + (m - 1)
        c, d = 1, 1
        n, m = min(n, m), max(n, m)
        for i in range(1, n):
            c *= (t - i + 1)
            d *= i
        return c // d



test_case = [
        (3,2,3),
        (7,3,28),
        (9, 8, 6435)
        ]

for m,n,s in test_case:
    r = Solution().uniquePaths(m, n)
    print(r, s)
    assert r == s
