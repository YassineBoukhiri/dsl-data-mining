from model.Classifier import Classifier
from model.DropoutLayer import DropoutLayer
from model.FlattenLayer import FlattenLayer
from model.Layer import Layer
from LayerBuilder import LayerBuilder
from itertools import product

class ClassifierBuilder:
    """
    Builder for the Classifier.
    """

    def __init__(self, root, rank):
        self.root = root
        self.rank = rank
        self.layers = dict()
        self.layers_count = 0
        self.dense_used = False
        self.conv_used = False
        self.max_pooling_used = False   
        self.dropout_used = False    
        self.flatten_used = False

    def dense(self, nb_neurons:int = None, activation:str = None):
        self.dense_used = True
        return LayerBuilder(self, self.layers_count).dense(nb_neurons, activation)

    def dropout(self, rate:float):
        if rate < 0 or rate > 1:
            raise ValueError("ERROR: The dropout rate must be between 0 and 1.")
        self.dropout_used = True
        self.add_layers([DropoutLayer(self.layers_count, rate)])
        return self

    def flatten(self):
        self.flatten_used = True
        self.add_layers([FlattenLayer(self.layers_count)])
        return self

    def add_layers(self, layers: list[Layer]):
        self.layers[self.layers_count] = layers
        self.layers_count += 1


    def compile(self):
        return self.root

    def build(self):
        neural_networks = list(product(*self.layers.values()))
        classifiers = []
        count = 0
        for neural_network in neural_networks:
            classifier = Classifier(self.rank, count +1)
            for layer in neural_network:
                classifier.add_layer(layer)
            classifiers.append(classifier)
            count += 1
        return classifiers
                
        

