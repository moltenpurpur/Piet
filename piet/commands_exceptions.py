from typing import *


class CommandsExceptions(Exception):
    def __init__(self, text):
        self.text = text
