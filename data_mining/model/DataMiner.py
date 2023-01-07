import os
from model.Notebookable import Notebookable


class DataMiner(Notebookable):

    def __init__(self):
        super().__init__()
        self.classifiers = []

    def dense(self):
        self.add_markdown_cell("""## Dense""")

    def add_classifier(self, classifier):
        self.classifiers.append(classifier)

    def last_classifier(self):
        return self.classifiers[-1]

    def get_notebook(self) -> str:
        self.add_markdown_cell("""## Data Mining""")
        for classifier in self.classifiers:
            self.add_code_cell(str(classifier.build()))
        return super().get_notebook()
        
        