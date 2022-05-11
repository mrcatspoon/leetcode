# https://leetcode.com/problems/design-parking-system/


class ParkingSystem:
    __slots__ = ("slots",)

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        self.slots[carType] -= 1
        return self.slots[carType] >= 0
