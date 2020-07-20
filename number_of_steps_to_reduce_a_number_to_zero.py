#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
class Solution:
    def numberOfSteps (self, num):
        if num == 0:
            return 0
        i = 0
        while num > 1:
            if num % 2:
                i+=2
                num = (num - 1) // 2
            else:
                num = num // 2
                i += 1
        return i + 1
