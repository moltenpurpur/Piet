from piet.pixels import Pixels
import argparse
from piet.piet_interpreter import PietInterpreter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Piet Interpreter')
    parser.add_argument('program',
                        help='путь до программы-картинки',
                        type=str)
    parser.add_argument('block_size',
                        help='размер блока',
                        type=int)
    args = parser.parse_args()

    pixels = Pixels.pixels_from_picture(args.program, args.block_size)
    interpreter = PietInterpreter(pixels)
    interpreter.start()
