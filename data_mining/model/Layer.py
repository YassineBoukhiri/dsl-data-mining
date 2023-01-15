class Layer: 
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        description = "Layer: rank = " + str(self.rank) 
        if self.rank == 0:
            return "First " + description
        else:
            return description
        
    def __repr__(self):
        return self.__str__()
