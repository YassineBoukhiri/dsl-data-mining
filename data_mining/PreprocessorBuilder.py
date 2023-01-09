from model.Preprocessor import Preprocessor

class PreprocessorBuilder:
    """
    Builder for the preprocessor.
    """

    def __init__(self, root):
        self.root = root
        self.preprocessor = None

    def fit(self):
        if self.preprocessor is None:
            self.preprocessor = Preprocessor()
        self.preprocessor.fit()
        return self

    def build(self):
        return self.preprocessor

    
    def end(self):
        return self.root