from model.Transformer import Transformer

class TransformerBuilder:
    """
    Builder for the transformer.
    """

    def __init__(self, root):
        self.root = root
        self.transformer = None

    def flatten(self):
        if self.transformer is None:
            self.transformer = Transformer()
        self.transformer.flatten()
        return self

    def normalize(self):
        if self.transformer is None:
            self.transformer = Transformer()
        self.transformer.normalize()
        return self

    def build(self):
        return self.transformer

    
    def end(self):
        return self.root