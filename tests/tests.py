import unittest
from piet import commands, direction


class TestCommands(unittest.TestCase):
    def test_push_empty(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.push(None)
        self.assertEqual(comm.stack, [None])

    def test_push_int(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.push(5)
        self.assertEqual(comm.stack, [5])

    def test_pop_empty_stack(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.pop('val')
        self.assertEqual(comm.stack, [])

    def test_pop(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(0)
        len_stack = len(comm.stack)
        comm.pop('val')
        self.assertEqual(len(comm.stack), len_stack - 1)

    def test_add(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(5)
        comm.stack.append(6)
        comm.add('val')
        self.assertEqual(comm.stack, [11])

    def test_add_empty_stack(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(5)
        first_stack = comm.stack
        comm.add('val')
        self.assertEqual(comm.stack, first_stack)

    def test_subtract(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(6)
        comm.stack.append(2)
        comm.subtract('val')
        self.assertEqual(comm.stack, [4])

    def test_subtract_empty_stack(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(6)
        first_stack = comm.stack
        comm.subtract('val')
        self.assertEqual(comm.stack, first_stack)

    def test_subtract_negative_meaning(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(2)
        comm.stack.append(6)
        comm.subtract('val')
        self.assertEqual(comm.stack, [-4])

    def test_multiply(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(4)
        comm.stack.append(3)
        comm.multiply('val')
        self.assertEqual(comm.stack, [12])

    def test_multiply_empty_stack(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(6)
        first_stack = comm.stack
        comm.multiply('val')
        self.assertEqual(comm.stack, first_stack)

    def test_multiply_negative_meaning(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(2)
        comm.stack.append(-6)
        comm.multiply('val')
        self.assertEqual(comm.stack, [-12])

    def test_divide(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(6)
        comm.stack.append(3)
        comm.divide('val')
        self.assertEqual(comm.stack, [2])

    def test_divide_empty_stack(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(6)
        first_stack = comm.stack
        comm.divide('val')
        self.assertEqual(comm.stack, first_stack)

    def test_divide_negative_meaning(self):
        dp = direction.DirectionPointer()
        cc = direction.CodelChooser()
        comm = commands.Commands(dp, cc)
        comm.stack.append(-6)
        comm.stack.append(2)
        comm.divide('val')
        self.assertEqual(comm.stack, [-3])


class TestDP(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class TestCC(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class TestInterpreter(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class TestPixel(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
