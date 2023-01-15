from model.Layer import Layer

class FlattenLayer(Layer): 
    def __init__(self, rank):
        super().__init__(rank)

    def __str__(self):
        return "Flatten()"

    def __repr__(self):
        return self.__str__()
