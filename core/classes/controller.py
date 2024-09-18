from abc import ABC

from core.classes.pagen import Pagen


class Controller(Pagen, ABC):
    def __init__(self):
        super().__init__()
