from data_mining.model.Classifier import Classifier

class KNNBuilder(Classifier):
    """
    Builder for the KNNBuilder.
    """

    def __init__(self, root, number):
        super().__init__(root, number)
        self.root = root
    

    def build(self):
        return super().build()
    

