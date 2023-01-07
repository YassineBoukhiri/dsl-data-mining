from model.Classifier import Classifier

class ClassifierBuilder:
    """
    Builder for the Classifier.
    """

    def __init__(self, root):
        self.root = root
        self.classifier = None

    def dense(self, nb_neurons, activation=None):
        if self.classifier is None:
            self.classifier = Classifier()
        self.classifier.add_dense_layer(nb_neurons, activation)
        return self

    def compile(self):
        return self.root

    def build(self):
        return self.classifier
