from model.Layer import Layer

class ConvLayer(Layer): 
    def __init__(self, rank, nb_neurons, activation = None, kernel_size = None):
        super().__init__(rank)
        self.nb_neurons = nb_neurons
        self.activation = activation if activation is not None else "relu"
        self.kernel_size = kernel_size

    def set_kernel_size(self, kernel_size):
        self.kernel_size = kernel_size

    def __str__(self):
        if self.rank == 0:
            return "Conv2D(" + str(self.nb_neurons) + (", kernel_size=" + str(self.kernel_size) if self.kernel_size is not None else "") + ", activation=\"" + str(self.activation) + "\", input_shape=X_train.shape[1:])"
        else:
            return "Conv2D(" + str(self.nb_neurons) + (", kernel_size=" + str(self.kernel_size) if self.kernel_size is not None else "") + ", activation=\"" + str(self.activation) + "\")"
        
    def __repr__(self):
        return self.__str__()
