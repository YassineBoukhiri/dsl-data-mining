import os


class Class:
    def __init__(self, name, dataset=None, count=None):
        self.dataset = None
        self.name = name
        if dataset is not None:
            self.dataset = dataset
        if count is None:
            self.count = len(os.listdir(f"{self.dataset}/{self.name}"))
        else:
            self.count = count

    def __repr__(self):
        return "class : " + self.name + " number of elements : " + str(self.count)
