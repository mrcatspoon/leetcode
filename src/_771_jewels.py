# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)

        jewels_counter = 0
        for stone in stones:
            if stone in jewels:
                jewels_counter += 1

        return jewels_counter
