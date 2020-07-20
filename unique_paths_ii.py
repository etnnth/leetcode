# https://leetcode.com/problems/unique-paths-ii/


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        I = len(obstacleGrid)
        J = len(obstacleGrid[0])
        self.cache = {}
        def moves(i,j):
            m = 0
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            if i == I - 1 and j == J - 1 and obstacleGrid[i][j] == 0:
                m += 1
            elif obstacleGrid[i][j] == 0:
                if i < I - 1:
                    m += moves(i + 1, j)
                if j < J - 1:
                    m += moves(i, j + 1)
            self.cache[(i,j)] = m
            return m
        return moves(0,0)


test_case = [
        (
        [[0,0,0],
        [0,1,0],
        [0,0,0]],
        2
            ),
        (
        [[1]],
        0
            ),
        (
        [[0,0],[0,0]],
        2
            )
        ]

for m,s in test_case:
    r = Solution().uniquePathsWithObstacles(m)
    print(s,r)
    assert s == r 
