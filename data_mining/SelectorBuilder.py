from model.Selector import Selector
from model.Class import Class
import os

class SelectorBuilder:
    """
    Builder for the selector.
    """

    def __init__(self, root):
        self.root = root
        self.selector = None
        # DSL validators
        self.select_all_used = False
        self.select_used = False

    def select_all(self):
        if self.select_all_used:
            raise Exception("You can't use select_all() twice.")
        if self.select_used:
            raise Exception("You can't use select_all() after select().")
        self.select_all_used = True
        available_classes = self.get_classes()
        if self.selector is None:
                self.selector = Selector()
        for class_ in available_classes:
            self.selector.add_class(Class(class_))
        return self

    def select(self, class_, count = None) :
        if self.select_all_used:
            raise Exception("You can't use select() after select_all().")
        self.select_used = True
        available_classes = self.get_classes()
        if class_ not in available_classes:
            raise Exception(f"Class {class_} not found.")
        if self.selector is None:
            self.selector = Selector()
        self.selector.add_class(Class(class_, count))
        return self

    def build(self):
        return self.selector
    
    def get_classes(self) -> list:
        return os.listdir("../input_data")

    def test_size(self, test_size):
        self.selector.set_test_size(test_size)
        return self
    
    def end(self):
        return self.root