# https://leetcode.com/problems/fancy-sequence/
from typing import List

MODULO = 10 ** 9 + 7


class Fancy:
    __slots__ = ("_data", "_add", "_multi")

    def __init__(self):
        self._data: List[int] = []
        self._add = 0
        self._multi = 1

    def append(self, val: int) -> None:
        self._data.append((val - self._add) * pow(self._multi, -1, MODULO))

    def addAll(self, inc: int) -> None:
        self._add += inc

    def multAll(self, m: int) -> None:
        self._add = self._add * m % MODULO
        self._multi = self._multi * m % MODULO

    def getIndex(self, idx: int) -> int:
        try:
            element = self._data[idx]
        except IndexError:
            return -1
        return (self._multi * element + self._add) % MODULO
