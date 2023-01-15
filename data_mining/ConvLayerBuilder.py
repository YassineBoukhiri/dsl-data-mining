from model.ConvLayer import ConvLayer
from LayerBuilder import LayerBuilder

class ConvLayerBuilder(LayerBuilder):
    """
    Builder for the convulutional layer.
    """

    def __init__(self, root, rank):
        super().__init__(root, rank)
        self.layers = []
        self.kernel_size_ = None
        self.kernel_size_used = False
        

    def conv(self, nb_neurons:int = None, activation:str = None):
        if self.done :
            self.build()
            self.root.add_layers(self.layers)
            return self.root.conv(nb_neurons, activation)
        if nb_neurons is None and activation != None:
            raise ValueError("ERROR: The number of neurons must be specified in order to add the activation function.")
        elif nb_neurons is not None:
            for i in range(self.multi_activation(activation)[0]):
                self.layers.append(ConvLayer(self.rank, nb_neurons, self.multi_activation(activation)[1][i]))
            return self
        else :
            self.done = True
            return self


    def activation(self, activation:str):
        if self.activation_used:
            raise ValueError("ERROR: The activation function can only be specified once.")
        else :
            self.activations_ = activation.split("|")
            self.activations_ = [activation.strip() for activation in self.activations_]
            self.activation_used = True
            self.set_just_used_false()
            return self

    def kernel_size(self, i:int, j:int):
        if self.kernel_size_:
            raise ValueError("ERROR: The kernel size can only be specified once.")
        else :
            self.kernel_size_ = (i, j)
            for layer in self.layers:
                layer.set_kernel_size((i, j))
            self.kernel_size_ = True
            self.set_just_used_false()
            return self


    def build(self):
        if self.range_used:
            for i in range(self.range_[0], self.range_[1], self.range_[2]):
                for activation in self.activations_:
                    self.layers.append(ConvLayer(self.rank, i, activation, self.kernel_size_))
        elif self.values_used:
            for i in self.values_:
                for activation in self.activations_:
                    self.layers.append(ConvLayer(self.rank, i, activation, self.kernel_size_))            
        return self.layers

    def compile(self):
        self.build()
        self.root.add_layers(self.layers)
        return self.root.compile()

    def max_pooling(self, i:int = None, j:int = None):
        self.build()
        self.root.add_layers(self.layers)
        return self.root.max_pooling(i, j)
