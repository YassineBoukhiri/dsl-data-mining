from model.Layer import Layer

class DenseLayer(Layer): 
    def __init__(self, rank, nb_neurons, activation = None):
        super().__init__(rank)
        self.nb_neurons = nb_neurons
        self.activation = activation if activation is not None else "relu"

    def __str__(self):
        if self.rank == 0:
            return "Dense(" + str(self.nb_neurons) + ", activation=\"" + str(self.activation) + "\", input_shape=(X_train.shape[1],))"
        else:
            return "Dense(" + str(self.nb_neurons) + ", activation=\"" + str(self.activation) + "\")"
        
    def __repr__(self):
        return self.__str__()
