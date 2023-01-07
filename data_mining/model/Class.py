import os

class Class: 
    def __init__(self, name, count=None):
        self.name = name
        if count is None:
            self.count = len(os.listdir(f"../input_data/{name}"))
        else:
            self.count = count
    
    def __repr__(self):
        return "class : " + self.name + " number of elements : " + str(self.count)