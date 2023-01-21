from SelectorBuilder import SelectorBuilder
from PreprocessorBuilder import PreprocessorBuilder
from TransformerBuilder import TransformerBuilder
from DataMinerBuilder import DataMinerBuilder
from ComparatorBuilder import ComparatorBuilder
from model.Deployer import Deployer
from model.App import App


class AppBuilder:
    """
    Builder for the application.
    """

    def __init__(self, name):
        self.name = name
        self.selector = None
        self.preprocessor = None
        self.transformer = None
        self.data_miner = None
        self.comparator = None
        self.deployer = None
    
    def select(self):
        self.selector = SelectorBuilder(self)
        return self.selector

    def preprocess(self):
        self.preprocessor = PreprocessorBuilder(self)
        return self.preprocessor
    
    def transform(self):
        self.transformer = TransformerBuilder(self)
        return self.transformer

    def create_model(self):
        self.data_miner = DataMinerBuilder(self)
        return self.data_miner

    def compare(self):
        self.comparator = ComparatorBuilder(self)
        return self.comparator

    def deploy_best(self, name = None):
        if name is None:
            name = self.name
        self.deployer = Deployer(name)
        return self
    
    def build(self):
        app = App(self.name, 
                    self.selector.build(), 
                    self.preprocessor.build(),
                    self.transformer.build(), 
                    self.data_miner.build(),
                    self.comparator.build(),
                    self.deployer)
        app.generate()
        print("INFO: Notebook generated successfully.")
    

    def __repr__(self) -> str:
        return App.__repr__(self)

    def __str__(self) -> str:
        return self.__repr__()
