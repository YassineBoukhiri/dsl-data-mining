from model.Notebookable import Notebookable


class DataMiner(Notebookable):

    def __init__(self):
        super().__init__()
        self.classifiers = []
        self.dense_used = False

    def add_classifier(self, classifier):
        self.classifiers.append(classifier)

    def last_classifier(self):
        return self.classifiers[-1]

    def get_imports_cell(self):
        imports = "from tensorflow.keras.models import Sequential"
        if self.dense_used:
            imports += "\nfrom tensorflow.keras.layers import Dense"
        return imports

    def set_dense_used(self):
        for classifier in self.classifiers:
            if classifier.dense_used:
                self.dense_used = True
                break

    def get_notebook(self) -> str:
        self.set_dense_used()
        self.add_markdown_cell("""## Data Mining""")
        self.add_code_cell(self.get_imports_cell())
        for classifier in self.classifiers:
            self.add_notebook(classifier.build().get_notebook())
        return super().get_notebook()
        
        