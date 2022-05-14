# https://leetcode.com/problems/flood-fill/
from typing import Generator, List, Tuple

Image = List[List[int]]


class Solution:
    __slots__ = ("_visited",)

    def __init__(self):
        self._visited = set()

    def floodFill(self, image: Image, sr: int, sc: int, newColor: int) -> List[List[int]]:
        target = image[sr][sc]
        if newColor != target:
            self.flood(image, sr, sc, target, newColor)
        return image

    def flood(self, image: Image, i: int, j: int, target: int, new_value: int):
        if image[i][j] != target or (i, j) in self._visited:
            return
        if image[i][j] == target:
            image[i][j] = new_value
        for ii, jj in self._yield_directions(image, i, j):
            self.flood(image, ii, jj, target, new_value)
            self._visited.add((ii, jj))

    def _yield_directions(self, image: Image, i: int, j: int) -> Generator[Tuple[int, int], None, None]:
        if i > 0:
            yield i - 1, j
        if i < len(image) - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < len(image[0]) - 1:
            yield i, j + 1
