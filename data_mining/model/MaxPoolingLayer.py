from model.Layer import Layer

class MaxPoolingLayer(Layer): 
    def __init__(self, rank, i, j):
        super().__init__(rank)
        self.pool_size = (i, j) if i is not None and j is not None else None

    def set_pool_size(self, pool_size):
        self.pool_size = pool_size

    def __str__(self):
        if self.pool_size is None:
            return "MaxPooling2D()"
        return "MaxPooling2D(" + str(self.pool_size) + ")"

    def __repr__(self):
        return self.__str__()
