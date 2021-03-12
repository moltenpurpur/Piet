from piet.pixels import Pixels, Pixel
from piet.colors import Color, Tone
from piet.piet_interpreter import PietInterpreter

p = Pixels([[Pixel(Color.green, Tone.light), Pixel(Color.green, Tone.light),
             Pixel(Color.green, Tone.light),
             Pixel(Color.green, Tone.light),
             Pixel(Color.green, Tone.normal), Pixel(Color.yellow, Tone.dark),
             Pixel(Color.black, Tone.light)],
            [Pixel(Color.white, Tone.light), Pixel(Color.white, Tone.light),
             Pixel(Color.white, Tone.light),
             Pixel(Color.white, Tone.light),
             Pixel(Color.black, Tone.light), Pixel(Color.white, Tone.light),
             Pixel(Color.black, Tone.light)],
            [Pixel(Color.white, Tone.light), Pixel(Color.white, Tone.light),
             Pixel(Color.white, Tone.light),
             Pixel(Color.black, Tone.light),
             Pixel(Color.white, Tone.light), Pixel(Color.white, Tone.light),
             Pixel(Color.black, Tone.light)],
            [Pixel(Color.white, Tone.light), Pixel(Color.white, Tone.light),
             Pixel(Color.white, Tone.light),
             Pixel(Color.white, Tone.light),
             Pixel(Color.black, Tone.light), Pixel(Color.black, Tone.light),
             Pixel(Color.black, Tone.light)]])

p1 = Pixels.pixels_from_picture('\programs\hello_medium.gif', 4)
intorp = PietInterpreter(p1)
intorp.start()
