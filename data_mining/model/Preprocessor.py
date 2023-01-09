from model.Notebookable import Notebookable

class Preprocessor(Notebookable):

    def __init__(self):
        super().__init__()
        self.fitted = False
        
    
    def fit(self):
        self.fitted = True
        return self

    def get_notebook(self) -> str:
        self.add_markdown_cell("""## Preprocessing of data""")
        if self.fitted:
            self.add_code_cell("""from sklearn.preprocessing import LabelEncoder\nle = LabelEncoder()\nY_train = le.fit_transform(Y_train)\nY_test = le.fit_transform(Y_test)""")
        return super().get_notebook()
            
    
        