from abc import ABC

from core.classes.pagen import Pagen
from core.lexicon.load_lexicon import Lexicon


class Controller(Pagen, ABC, Lexicon):
    def __init__(self):
        super().__init__()
