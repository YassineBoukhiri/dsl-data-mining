from model.Notebookable import Notebookable
from ClassifierBuilder import ClassifierBuilder

class DataMiner(Notebookable):

    def __init__(self):
        super().__init__()
        self.classifiers: ClassifierBuilder = []
        self.dense_used = False
        self.conv_used = False
        self.max_pooling_used = False
        self.dropout_used = False
        self.flatten_used = False

    def add_classifier(self, classifier):
        self.classifiers.append(classifier)

    def last_classifier(self) -> ClassifierBuilder:
        return self.classifiers[-1]

    def get_imports_cell(self):
        imports = "from tensorflow.keras.models import Sequential"
        if self.dense_used:
            imports += "\nfrom tensorflow.keras.layers import Dense"
        if self.conv_used:
            imports += "\nfrom tensorflow.keras.layers import Conv2D"
        if self.max_pooling_used:
            imports += "\nfrom tensorflow.keras.layers import MaxPooling2D"
        if self.dropout_used:
            imports += "\nfrom tensorflow.keras.layers import Dropout"
        if self.flatten_used:
            imports += "\nfrom tensorflow.keras.layers import Flatten"
        imports += "\nimport matplotlib.pyplot as plt"
        return imports

    def set_used_parameters(self):
        for classifier in self.classifiers:
            if classifier.dense_used:
                self.dense_used = True
            if classifier.conv_used:
                self.conv_used = True
            if classifier.max_pooling_used:
                self.max_pooling_used = True
            if classifier.dropout_used:
                self.dropout_used = True
            if classifier.flatten_used:
                self.flatten_used = True

    def code_plotting_metrics(self):
        result = "# Plot accuracy in the same graph"
        result += "\nfor key, value in models_metrics.items():"
        result +=   "\n\thistory = value[0]"
        result +=   "\n\tplt.plot(history.history['accuracy'])"
        result += "\nplt.title('model accuracy')"
        result += "\nplt.ylabel('accuracy')"
        result += "\nplt.xlabel('epoch')"
        result += "\nplt.legend(models_metrics.keys(), loc='upper left')"
        result += "\nplt.show()"

        result += "\n\n# Plot loss in the same graph"
        result += "\nfor key, value in models_metrics.items():"
        result +=   "\n\thistory = value[0]"
        result +=   "\n\tplt.plot(history.history['loss'])"
        result += "\nplt.title('model loss')"
        result += "\nplt.ylabel('loss')"
        result += "\nplt.xlabel('epoch')"
        result += "\nplt.legend(models_metrics.keys(), loc='upper left')"
        result += "\nplt.show()"
        return result



    def get_notebook(self) -> str:
        self.set_used_parameters()
        self.add_markdown_cell("""## Data Mining""")
        self.add_code_cell(self.get_imports_cell())
        self.add_markdown_cell("""### Keeping track of the metrics""")
        self.add_code_cell("""models_metrics = dict()""")
        for classifierBuilder in self.classifiers:
            for classifier in classifierBuilder.build():
                self.add_notebook(classifier.get_notebook())
        self.add_markdown_cell("""### Plotting the metrics""")
        self.add_code_cell(self.code_plotting_metrics())
        return super().get_notebook()
        
        