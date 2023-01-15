from model.DataMiner import DataMiner
from ANNBuilder import ANNBuilder
from CNNBuilder import CNNBuilder


class DataMinerBuilder:
    """
    Builder for the DataMiner.
    """

    def __init__(self, root):
        self.root = root
        self.data_miner = DataMiner()

    def ANN(self):
        self.data_miner.add_classifier(ANNBuilder(self, len(self.data_miner.classifiers) + 1))
        return self.data_miner.last_classifier()

    def CNN(self):
        self.data_miner.add_classifier(CNNBuilder(self, len(self.data_miner.classifiers) + 1))
        return self.data_miner.last_classifier()
        


    def build(self):
        return self.data_miner

    
    def end(self):
        return self.root