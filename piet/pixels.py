from typing import *
from piet.colors import Color, Tone
from piet.direction import Point
from PIL import Image


class Pixel:
    def __init__(self, color: Color, tone: Tone):
        self.color = color
        self.tone = tone

    def __eq__(self, other):
        return self.color == other.color and self.tone == other.tone

    colors = {(255, 192, 192): (Tone.light, Color.red),
              (255, 255, 192): (Tone.light, Color.yellow),
              (192, 255, 192): (Tone.light, Color.green),
              (192, 255, 255): (Tone.light, Color.cyan),
              (192, 192, 255): (Tone.light, Color.blue),
              (255, 192, 255): (Tone.light, Color.magenta),
              (255, 0, 0): (Tone.normal, Color.red),
              (255, 255, 0): (Tone.normal, Color.yellow),
              (0, 255, 0): (Tone.normal, Color.green),
              (0, 255, 255): (Tone.normal, Color.cyan),
              (0, 0, 255): (Tone.normal, Color.blue),
              (255, 0, 255): (Tone.normal, Color.magenta),
              (192, 0, 0): (Tone.dark, Color.red),
              (192, 192, 0): (Tone.dark, Color.yellow),
              (0, 192, 0): (Tone.dark, Color.green),
              (0, 192, 192): (Tone.dark, Color.cyan),
              (0, 0, 192): (Tone.dark, Color.blue),
              (192, 0, 192): (Tone.dark, Color.magenta),
              (255, 255, 255): (Tone.normal, Color.white),
              (0, 0, 0): (Tone.normal, Color.black)}

    @classmethod
    def pixel_frog_rgb(cls, rgb: Tuple):
        if len(rgb) == 4:
            rgb = rgb[:-1]
        if rgb in cls.colors.keys():
            return Pixel(cls.colors[rgb][1], cls.colors[rgb][0])
        else:
            return Pixel(Color.black, Tone.light)


class Pixels:
    def __init__(self, pixels: List[List[Pixel]]):
        self.pixels = pixels

    @classmethod
    def pixels_from_picture(cls, picture_path: str, size=1):
        picture = []
        with Image.open(picture_path) as pic:
            im = pic.convert('RGB')
            for i in range(pic.size[1] // size):
                row = []
                for j in range(pic.size[0] // size):
                    row.append(
                        Pixel.pixel_frog_rgb(
                            im.getpixel((j * size, i * size))))
                picture.append(row)

        return cls(picture)

    def __getitem__(self, item: Point):
        return self.pixels[item.y][item.x]

    def is_point_inside(self, point: Point):
        return 0 <= point.y < len(self.pixels) \
               and 0 <= point.x < len(self.pixels[0])

    def find_neighbours(self, point: Point):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if abs(dx) == abs(dy):
                    continue
                d_point = Point(dx, dy)
                new_point = point + d_point
                if not self.is_point_inside(new_point):
                    continue
                if self[point] == self[new_point]:
                    yield new_point
