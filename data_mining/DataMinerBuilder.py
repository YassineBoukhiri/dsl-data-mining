from model.DataMiner import DataMiner
from ANNBuilder import ANNBuilder


class DataMinerBuilder:
    """
    Builder for the DataMiner.
    """

    def __init__(self, root):
        self.root = root
        self.data_miner = None

    def ANN(self):
        if self.data_miner is None:
            self.data_miner = DataMiner()
        self.data_miner.add_classifier(ANNBuilder(self))
        return self.data_miner.last_classifier()

    def build(self):
        return self.data_miner

    
    def end(self):
        return self.root