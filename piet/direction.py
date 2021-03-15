import enum
from typing import *


class Direction(enum.IntEnum):
    right = 0
    down = 1
    left = 2
    up = 3


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return self.x * 17 + self.y * 11

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class DirectionPointer:
    def __init__(self):
        self.direction_pointer: Direction = Direction.right

    def turn_direction_pointer(self, step: int = 1):
        directions_count = 4
        self.direction_pointer = \
            (self.direction_pointer + step) % directions_count

    def get_direction(self) -> Point:
        if self.direction_pointer == Direction.left:
            return Point(-1, 0)
        if self.direction_pointer == Direction.right:
            return Point(1, 0)
        if self.direction_pointer == Direction.up:
            return Point(0, -1)
        if self.direction_pointer == Direction.down:
            return Point(0, 1)


class CodelChooser:
    def __init__(self):
        self.codel_chooser = Direction.left

    def turn_codel_chooser(self, direction_of_rotation: int = 1):
        rotation_step = 2
        step, directions_count = rotation_step * direction_of_rotation, 4
        self.codel_chooser = (self.codel_chooser + step) % directions_count

    def get_direction(self) -> int:
        if self.codel_chooser == Direction.left:
            return -1
        return 1
