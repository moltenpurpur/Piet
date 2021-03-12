from typing import *
from piet.direction import DirectionPointer, CodelChooser
from piet.commands_exceptions import CommandsExceptions


class Commands:
    def __init__(self, dp, cc, stack):
        self.dp: DirectionPointer = DirectionPointer()
        self.cc: CodelChooser = CodelChooser()
        self.stack: List[int] = []
        self.codels_count: int = 0

        self.commands_table = [
            [self.p, self.push, self.pop],
            [self.add, self.subtract, self.multiply],
            [self.divide, self.mod, self.not_command],
            [self.greater, self.pointer, self.switch],
            [self.duplicate, self.roll, self.in_number],
            [self.in_char, self.out_number, self.out_char]
        ]

    def p(self, val):
        print("fff")

    def push(self,
             val):  # Помещает значение только что покинутого цветного блока в стек.
        self.stack.append(val)

    def pop(self, val):  # Извлекает верхнее значение из стека, удаляя его.
        self.stack.pop()

    def add(self,
            val):  # Извлекает два верхних значения из стека, складывает их и помещает результат обратно в стек.
        self.stack.append(
            self.stack.pop()
            + self.stack.pop())

    def subtract(
            self,
            val):  # Извлекает два верхних значения из стека, вычитает верхнее значение из второго, и помещает результат обратно в стек.
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        self.stack.append(v2 - v1)

    def multiply(self,
                 val):  # Извлекает два верхних значения из стека, умножает их и помещает результат обратно в стек.
        self.stack.append(
            self.stack.pop()
            * self.stack.pop())

    def divide(self,
               val):  # Извлекает два верхних значения из стека, вычисляет целочисленное деление второго значения на верхнее и помещает результат обратно в стек.
        self.stack.append(
            self.stack.pop(len(self.stack) - 2)
            // self.stack.pop())

    def mod(
            self,
            val):  # Извлекает два верхних значения из стека, находит остаток от деления второго числа на первое и помещает результат обратно в стек.
        self.stack.append(
            self.stack.pop(len(self.stack) - 2)
            % self.stack.pop())

    def not_command(self,
                    val):  # Заменяет стековое значение на ноль, если оно ненулевое, и на 1, если оно нулевое.
        element = self.stack.pop()
        if element == 0:
            self.stack.append(1)
        else:
            self.stack.append(0)

    def greater(self,
                val):  # Извлекает два значения и помещает 1, если второе значение больше первого, 0 - если не больше.

        if self.stack.pop() < self.stack.pop():
            self.stack.append(1)
        else:
            self.stack.append(0)

    def pointer(
            self,
            val):  # Извлекает значение и поворачивает по часовой стрелке DP на данное число, против часовой стрелки, если число отрицательное.
        self.dp.turn_direction_pointer(self.stack.pop())

    def switch(self, val):  # Переключает CC требуемое число раз
        self.cc.turn_codel_chooser(self.stack.pop())

    def duplicate(self, val):  # Помещает копию верхнего значения стека в стек
        element = self.stack[-1]
        self.stack.append(element)

    def roll(
            self,
            val):  # Извлекает два значения из стека (n — верхнее, m — второе) и помещает верхнее значение стека на глубину m n раз.
        print("ROOOOOL")

    def in_number(self, val):  # Читает число
        self.stack.append(int(input()))

    def in_char(
            self, val):  # Читает символ
        self.stack.append(ord(input()[0]))

    def out_number(self, val):  # выводит число
        print('out_num:' + str(self.stack.pop()))
        print()

    def out_char(self, val):  # выводит символ.
        print(chr(self.stack.pop()), end='')
