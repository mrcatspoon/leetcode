# https://leetcode.com/problems/max-area-of-island/
from typing import Generator, List, Set, Tuple

WATTER = 0
ISLAND = 1
Grid = List[List[int]]


class Solution:
    __slots__ = ("_visited",)

    def __init__(self):
        self._visited = set()

    def maxAreaOfIsland(self, grid: Grid) -> int:
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == WATTER or (i, j) in self._visited:
                    continue
                island_parts = set()
                self.get_island_size(grid, i, j, island_parts)
                size = len(island_parts)
                if size > max_size:
                    max_size = size
        return max_size

    def get_island_size(self, grid: Grid, i: int, j: int, island_parts: Set):
        if grid[i][j] != ISLAND or (i, j) in self._visited:
            return
        if grid[i][j] == ISLAND:
            island_parts.add((i, j))
        self._visited.add((i, j))
        for ii, jj in self._yield_directions(grid, i, j):
            self.get_island_size(grid, ii, jj, island_parts)
            self._visited.add((ii, jj))

    def _yield_directions(self, grid: Grid, i: int, j: int) -> Generator[Tuple[int, int], None, None]:
        if i > 0:
            yield i - 1, j
        if i < len(grid) - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < len(grid[0]) - 1:
            yield i, j + 1
