from model.Comparator import Comparator

class ComparatorBuilder:
    """
    Builder for the comparator.
    """

    def __init__(self, root):
        self.root = root
        self.comparator = Comparator()
        self.all_metrics_ = ["accuracy", "loss"]
        self.used_metrics = []
        self.when_used = False

    def all_metrics(self):
        self.used_metrics = self.all_metrics_
        return self


    def when(self):
        if self.when_used:
            raise ValueError("ERROR: The when can only be specified once.")
        self.when_used = True
        return self

    def accuracy(self, comparator, value):
        if not self.when_used:
            raise ValueError("ERROR: The accuracy must be specified after the when.")
        self.comparator.accuracy()
        return self

    def build(self):
        return self.comparator

    
    def end(self):
        return self.root