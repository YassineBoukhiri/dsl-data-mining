import os
from model.Notebookable import Notebookable


class Transformer(Notebookable):

    def __init__(self):
        super().__init__()
        self.flattened = False
        self.normalized = False
        self.reshaped = False
        self.dims = None
    
    def flatten(self):
        self.flattened = True
        return self

    def normalize(self):
        self.normalized = True
        return self

    def reshape(self, *dims):
        self.reshaped = True
        self.dims = dims
        return self

    def reshape_code(self):
        result = "X_train = X_train.reshape(X_train.shape[0]"
        for i, dim in enumerate(self.dims, start=1):
            result += ", " + (str(dim) if dim.strip() != "?" else "X_train.shape[" + str(i) + "]")
        result += ")\nX_test = X_test.reshape(X_test.shape[0]"
        for i, dim in enumerate(self.dims, start=1):
            result += ", " + (str(dim) if dim.strip() != "?" else "X_test.shape[" + str(i) + "]")
        result += ")\nprint(X_train.shape)\nprint(X_test.shape)"
        return result


    def get_notebook(self) -> str:
        self.add_markdown_cell("""## Transformation of data""")
        if self.flattened:
            self.add_markdown_cell("""### Flattening of data""")
            self.add_code_cell("""X_train = X_train.reshape(X_train.shape[0], -1)\nX_test = X_test.reshape(X_test.shape[0], -1)\nprint(X_train.shape)\nprint(X_test.shape)""")
        if self.normalized:
            self.add_markdown_cell("""### Normalization of data""")
            self.add_code_cell("""# Making sure that the values are float so that we can get decimal points after division\nX_train = X_train.astype('float32')\nX_test = X_test.astype('float32')\n# Normalizing the RGB codes by dividing it to the max RGB value.\nX_train = X_train / 255\nX_test = X_test / 255\nprint(X_train.shape)\nprint(X_test.shape)""")
        if self.reshaped:
            self.add_markdown_cell("""### Reshaping of data""")
            self.add_code_cell(self.reshape_code())
        return super().get_notebook()
    
        