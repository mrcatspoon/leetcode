# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num == 1:
                steps += 1
                break
            elif num % 2:
                num -= 1
                steps += 1
            num //= 2
            steps += 1

        return steps
