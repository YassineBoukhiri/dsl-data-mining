from model.ComparisonParameter import ComparisonParameter
from model.ComparisonParameter import Operator

class ComparisonParametersBuilder: 

    def __init__(self, root):
        self.root = root
        self.parameters: list[ComparisonParameter] = []
        self.accuracy_used = False
        self.loss_used = False
    
    def accuracy(self, comparator, value):
        if self.accuracy_used:
            raise ValueError("ERROR: The accuracy can only be specified once.")
        self.accuracy_used = True
        self.add_parameter("accuracy", comparator, value)
        return self

    def loss(self, comparator, value):
        if self.loss_used:
            raise ValueError("ERROR: The loss can only be specified once.")
        self.loss_used = True
        self.add_parameter("loss", comparator, value)
        return self

    def add_parameter(self, key, comparator, value):
        comparator = comparator.strip()
        if comparator not in ["<", "<=", "==", ">=", ">"]:
            raise ValueError("ERROR: The comparator must be one of the following: <, <=, ==, >=, >.")
        operator = Operator.from_string(comparator)
        self.parameters.append(ComparisonParameter(key, value=value, operator=operator))
        
    def end(self):
        return self.root.end()

