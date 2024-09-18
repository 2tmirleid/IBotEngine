import os

import yaml


class Lexicon:
    def __init__(self):
        self.lexicon = self.load_lexicon()

        self.buttons = self.lexicon.get('buttons')
        self.callback_data = self.lexicon.get('callback_data')
        self.replicas = self.lexicon.get('replicas')

    def load_lexicon(self) -> dict:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'lexicon.yaml')

        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
