from model.DenseLayer import DenseLayer

class LayerBuilder:
    """
    Builder for the layer.
    """

    def __init__(self, root, rank):
        self.root = root
        self.rank = rank
        self.range_ = None
        self.values_ = None
        self.range_used = False
        self.values_used = False
        self.range_just_used = False
        self.values_just_used = False
        self.step_used = False
        self.activations_ = [None]
        self.activation_used = False
        self.layers = []
        self.done = False
        

    def range(self, start: int, end: int):
        if self.range_used:
            raise ValueError("ERROR: The range can only be specified once.")
        if self.values_used:
            raise ValueError("ERROR: The range and the values can't be specified together.")
        self.range_ = (start, end)
        self.range_used = True
        self.range_just_used = True
        return self
    
    def values(self, *values):
        if self.values_used:
            raise ValueError("ERROR: The values can only be specified once.")
        if self.range_used:
            raise ValueError("ERROR: The range and the values can't be specified together.")
        self.values_ = values
        self.values_used = True
        self.values_just_used = True
        return self

    def conv(self, nb_neurons:int = None, activation:str = None):
        self.build()
        self.root.add_layers(self.layers)
        return self.root.conv(nb_neurons, activation)

    

    def step(self, step:int):
        if self.step_used:
            raise ValueError("ERROR: The step can only be specified once.")
        if self.values_used:
            raise ValueError("ERROR: The step must be specified after the range.")
        if self.range_just_used:
            self.range_ = (self.range_[0], self.range_[1], step)
            self.step_used = True
            self.set_just_used_false()
            return self
        else:
            raise ValueError("ERROR: The step must be specified after the range.")

    def multi_activation(self, activation: str) :
        if activation is None:
            return 1, [None]
        if "|" not in activation:
            return 1, [activation]
        else:
            activations = activation.split("|")
            activations = [activation.strip() for activation in activations]
            return len(activations), activations

    
    def activation(self, activation:str):
        if self.activation_used:
            raise ValueError("ERROR: The activation function can only be specified once.")
        else :
            self.activations_ = activation.split("|")
            self.activations_ = [activation.strip() for activation in self.activations_]
            self.activation_used = True
            self.set_just_used_false()
            self.build()
            self.root.add_layers(self.layers)
            return self.root

        

    def dense(self, nb_neurons:int = None, activation:str = None):
        if self.done :
            self.build()
            self.root.add_layers(self.layers)
            return self.root.dense(nb_neurons, activation)
        if nb_neurons is None and activation != None:
            raise ValueError("ERROR: The number of neurons must be specified in order to add the activation function.")
        elif nb_neurons is not None:
            for i in range(self.multi_activation(activation)[0]) :
                self.layers.append(DenseLayer(self.rank, nb_neurons, self.multi_activation(activation)[1][i]))
            self.done = True
            return self
        else :
            self.done = True
            return self

    def compile(self):
        self.build()
        self.root.add_layers(self.layers)
        return self.root.compile()

    def set_just_used_false(self):
        self.range_just_used = False
        self.values_just_used = False

    def build(self):
        if self.range_used:
            for i in range(self.range_[0], self.range_[1], self.range_[2]):
                for activation in self.activations_:
                    self.layers.append(DenseLayer(self.rank, i, activation))
        elif self.values_used:
            for i in self.values_:
                for activation in self.activations_:
                    self.layers.append(DenseLayer(self.rank, i, activation))
        return self.layers