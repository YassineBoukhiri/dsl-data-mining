

class Classifier:

    def __init__(self):
        self.layers = []

    def add_dense_layer(self, nb_neurons, activation=None):
        if activation is None:
            activation = "relu"
        self.layers.append("Dense(" + str(nb_neurons) + ", activation=" + str(activation) + ")")

    def __str__(self):
        result = "model = Sequential()\n"
        for layer in self.layers:
            result += "model.add(" + layer + ")\n"
        return result

    
        