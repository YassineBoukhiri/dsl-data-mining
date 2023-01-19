from model.Notebookable import Notebookable
from model.ComparisonParameter import ComparisonParameter

class Comparator(Notebookable):

    def __init__(self, parameters: list[ComparisonParameter] = []):
        super().__init__()
        parameters = parameters

    def get_parameter_by_name(self, name: str) -> ComparisonParameter:
        for parameter in self.parameters:
            if parameter.name == name:
                return parameter
        return None

    def get_notebook(self) -> str:
        self.add_markdown_cell("""## Preprocessing of data""")
        if self.fitted:
            self.add_code_cell("""from sklearn.preprocessing import LabelEncoder\nle = LabelEncoder()\nY_train = le.fit_transform(Y_train)\nY_test = le.fit_transform(Y_test)""")
        return super().get_notebook()