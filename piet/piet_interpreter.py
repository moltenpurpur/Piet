from piet.pixels import Pixels
from piet.direction import DirectionPointer, CodelChooser, Direction, Point
from piet.commands import Commands
from piet.colors import Color, Tone
from typing import *


class PietInterpreter:

    def __init__(self, pixels: Pixels):
        self.dp = DirectionPointer()
        self.cc = CodelChooser()
        self.pixels = pixels
        self.commands = Commands(self.dp, self.cc)
        self.current_pos = Point(0, 0)

    def get_blocks(self) -> List:
        stack: List[Point] = list()
        visited: Set[Point] = set()
        stack.append(self.current_pos)
        count = 0
        while len(stack) != 0:
            current = stack.pop()
            count += 1
            visited.add(current)
            for neighbor in self.pixels.find_neighbours(current):
                if neighbor not in visited:
                    stack.append(neighbor)
        return list(visited)

    def chose_next_block(self, blocks: List[Point]) -> Point:
        dp_points = list()

        if self.dp.direction_pointer in (Direction.left, Direction.right):
            blocks.sort(key=lambda point: point.x)
            if self.dp.direction_pointer == Direction.right:
                blocks.reverse()
            for block in blocks:
                if len(dp_points) == 0 or block.x == dp_points[-1].x:
                    dp_points.append(block)
            dp_points.sort(key=lambda point: point.y)

        else:
            blocks.sort(key=lambda point: point.y)
            if self.dp.direction_pointer == Direction.down:
                blocks.reverse()
            for block in blocks:
                if len(dp_points) == 0 or block.y == dp_points[-1].y:
                    dp_points.append(block)
            dp_points.sort(key=lambda point: point.x)

        if self.dp.direction_pointer in (Direction.right, Direction.up):
            if self.cc.codel_chooser == Direction.right:
                return dp_points[-1]
            else:
                return dp_points[0]

        else:
            if self.cc.codel_chooser == Direction.left:
                return dp_points[-1]
            else:
                return dp_points[0]

    def execute_command(self, next_block: Point, blocks_count: int):
        color_step = self.pixels[next_block].color - \
                     self.pixels[self.current_pos].color
        if color_step < 0:
            color_step = 6 + color_step

        tone_step = self.pixels[next_block].tone - \
                    self.pixels[self.current_pos].tone
        if tone_step < 0:
            ton_step = 3 + tone_step

        command = self.commands.commands_table[color_step][tone_step]
        command(blocks_count)

    def start(self):
        turn_number = 0
        blocks = list()
        while turn_number < 8:
            if turn_number == 0:
                blocks = self.get_blocks()
            next_block = self.chose_next_block(
                blocks)

            next_block = next_block + self.dp.get_direction()
            if not self.pixels.is_point_inside(next_block) \
                    or self.pixels[next_block].color == Color.black:
                if turn_number % 2 != 0:
                    self.dp.turn_direction_pointer()
                else:
                    self.cc.turn_codel_chooser()
                turn_number += 1
            elif self.pixels[next_block].color not in [Color.black,
                                                       Color.white]:
                self.execute_command(next_block, len(blocks))
                self.current_pos = next_block
                turn_number = 0
            else:
                if self.pass_white(next_block):
                    break
                else:
                    turn_number = 0

    def pass_white(self, next_block):
        visited: Set[Tuple[Point, Direction]] = set()
        visited.add((next_block, self.dp.direction_pointer))
        while True:
            new_next_block = next_block + self.dp.get_direction()
            if (new_next_block, self.dp.direction_pointer) in visited:
                return True
            if not self.pixels.is_point_inside(new_next_block) \
                    or self.pixels[new_next_block].color == Color.black:
                self.dp.turn_direction_pointer()
            elif self.pixels[new_next_block].color != Color.white:
                self.current_pos = new_next_block
                return False
            else:
                visited.add((new_next_block, self.dp.direction_pointer))
                next_block = new_next_block
