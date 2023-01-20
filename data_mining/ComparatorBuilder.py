from MetricsBuilder import MetricsBuilder
from ComparisonParametersBuilder import ComparisonParametersBuilder
from model.Comparator import Comparator

class ComparatorBuilder:
    """
    Builder for the comparator.
    """

    def __init__(self, root):
        self.root = root
        self.comparator = Comparator()
        self.metrics_builder = None
        self.parameters_builder = None
        self.all_metrics_ = ["accuracy", "loss"]
        self.used_metrics = []
        self.all_metrics_used_validator = False
        self.metrics_used_validator = False
        self.when_used = False

    def all_metrics(self):
        if self.all_metrics_used_validator:
            raise ValueError("ERROR: The all_metrics can only be specified once.")
        if self.metrics_used_validator:
            raise ValueError("ERROR: The all_metrics and metrics can not be specified together.")
        self.all_metrics_used_validator = True
        self.used_metrics = self.all_metrics_
        return self

    def metrics(self):
        if self.all_metrics_used_validator:
            raise ValueError("ERROR: The all_metrics and metrics can not be specified together.")
        if self.metrics_used_validator:
            raise ValueError("ERROR: The metrics can only be specified once.")
        self.metrics_used_validator = True
        self.metrics_builder = MetricsBuilder(self)
        return self.metrics_builder


    def when(self):
        if self.when_used:
            raise ValueError("ERROR: The when can only be specified once.")
        self.when_used = True
        self.parameters_builder = ComparisonParametersBuilder(self)
        return self.parameters_builder
        return self

    def accuracy(self, comparator, value):
        if not self.when_used:
            raise ValueError("ERROR: The accuracy must be specified after the when.")
        self.comparator.accuracy()
        return self

    def build(self):
        return self.comparator

    
    def end(self):
        # Setting the metrics
        if self.metrics_builder:
            self.used_metrics = self.metrics_builder.metrics
        elif self.used_metrics == []:
            self.used_metrics = self.all_metrics_
        self.comparator.metrics = self.used_metrics
        # Setting the parameters
        if self.parameters_builder:
            self.comparator.parameters = self.parameters_builder.parameters
        return self.root