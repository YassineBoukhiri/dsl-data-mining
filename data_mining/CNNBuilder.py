from ClassifierBuilder import ClassifierBuilder
from ConvLayerBuilder import ConvLayerBuilder
from model.MaxPoolingLayer import MaxPoolingLayer


class CNNBuilder(ClassifierBuilder):
    """
    Builder for the CNNBuilder.
    """

    def __init__(self, root, number):
        super().__init__(root, number)
        self.root = root
    
    def conv(self, nb_neurons:int = None, activation:str = None):
        self.conv_used = True
        return ConvLayerBuilder(self, self.layers_count).conv(nb_neurons, activation)

    def max_pooling(self, i:int = None, j:int = None):
        if (i is None and j is not None) or (i is not None and j is None):
            raise ValueError("ERROR: You must specify either the two dimensions of the pooling layer or none of them.")
        self.add_layers([MaxPoolingLayer(self.layers_count, i, j)])
        self.max_pooling_used = True
        return self

    def build(self):
        return super().build()
    

