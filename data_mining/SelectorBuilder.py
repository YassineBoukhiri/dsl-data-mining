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

    def acquire_data(self, dataset):
        if self.selector is None:
            self.selector = Selector()
        self.selector.set_dataset(dataset)
        return self

    def all_classes(self):
        if self.select_all_used:
            raise Exception("You can't use all_classes() twice.")
        if self.select_used:
            raise Exception("You can't use all_classes() after class_().")
        self.select_all_used = True
        available_classes = self.get_classes()
        if self.selector is None:
            self.selector = Selector()
        for class_ in available_classes:
            self.selector.add_class(
                Class(class_, self.selector.dataset))
        return self

    def class_(self, class_, count=None):
        if self.select_all_used:
            raise Exception("You can't use class_() after all_classes().")
        self.select_used = True
        available_classes = self.get_classes()
        if class_ not in available_classes:
            raise Exception(f"Class {class_} not found.")
        if self.selector is None:
            self.selector = Selector()
        self.selector.add_class(Class(class_, self.selector.dataset, count))
        return self

    def build(self):
        return self.selector

    def get_classes(self) -> list:
        dataset_dir = "input_data"
        try:
            if self.selector is not None:
                dataset_dir = self.selector.dataset
            return os.listdir(dataset_dir)
        except:
            raise Exception("Dataset not found.")

    def test_split(self, test_size):
        self.selector.set_test_size(test_size)
        return self

    def end(self):
        return self.root
