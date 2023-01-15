from model.Layer import Layer

class DropoutLayer(Layer): 
    def __init__(self, rank, value):
        super().__init__(rank)
        self.pool_size = value

    def __str__(self):
        return "Dropout(" + str(self.pool_size) + ")"

    def __repr__(self):
        return self.__str__()
