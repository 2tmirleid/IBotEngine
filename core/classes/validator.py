from core.lexicon.load_lexicon import load_lexicon


class Validator:
    def __init__(self):
        self.lexicon = load_lexicon()
        self.replicas = self.lexicon.get('replicas')
