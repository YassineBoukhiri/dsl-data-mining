from model.Notebookable import Notebookable
from model.Layer import Layer

class Classifier(Notebookable):

    def __init__(self, rank, number, reshaped = False, dims = None, flattened = False):
        super().__init__()
        self.name = "Classifier"
        self.rank = rank
        self.number = number
        self.reshaped = reshaped
        self.flattened = flattened
        self.dims = dims
        self.layers = []

    def add_layer(self, layer: Layer):
        self.layers.append(layer)

    def reshape(self, *dims):
        if len(dims) == 0:
            raise ValueError("ERROR: The reshape method must have at least one dimension.")
        if self.reshaped:
            raise ValueError("ERROR: The reshape method can only be called once.")
        if self.flattened:
            raise ValueError("ERROR: The reshape method can't be called after the flatten method.")
        self.reshaped = True
        self.dims = dims
        return self

    def flatten(self):
        if self.flattened:
            raise ValueError("ERROR: The flatten method can only be called once.")
        if self.reshaped:
            raise ValueError("ERROR: The flatten method can't be called after the reshape method.")
        self.flattened = True
        return self

    def reshaped_code(self):
        result = "X_train_save = X_train\nX_test_save = X_test\n"
        result += "X_train = X_train.reshape(X_train.shape[0]"
        for i, dim in enumerate(self.dims, start=1):
            result += ", " + (str(dim) if str(dim).strip() != "?" else "X_train.shape[" + str(i) + "]")
        result += ")\nX_test = X_test.reshape(X_test.shape[0]"
        for i, dim in enumerate(self.dims, start=1):
            result += ", " + (str(dim) if str(dim).strip() != "?" else "X_test.shape[" + str(i) + "]")
        result += ")\nprint(X_train.shape)\nprint(X_test.shape)"
        return result

    def flatten_code(self):
        result = "X_train_save = X_train\nX_test_save = X_test\nX_train = X_train.reshape(X_train.shape[0], -1)\nX_test = X_test.reshape(X_test.shape[0], -1)\nprint(X_train.shape)\nprint(X_test.shape)"
        return result
        

    def create_model_code(self):
        result = "model = Sequential()"
        for layer in self.layers:
            result += "\nmodel.add(" + str(layer) + ")"
        result += "\nmodel.compile(optimizer=\"adam\", loss=\"sparse_categorical_crossentropy\", metrics=[\"accuracy\"])"
        result += "\nmodel.summary()"
        return result

    def train_and_evaluate_model_code(self):
        result = "history = model.fit(X_train, Y_train, epochs=10, batch_size=32)"
        result += "\nscore = model.evaluate(X_test, Y_test)"
        result += "\nprint(\"Loss : \", score[0])"
        result += "\nprint(\"Accuracy : \", score[1])"
        result += "\nmodels_metrics[\"" + str(self.rank) +"-"+ str(self.number) + "\"] = [history, score, model]"
        result += "\nX_train = X_train_save\nX_test = X_test_save" if self.reshaped or self.flattened else ""
        return result


    def get_notebook(self) -> str:
        self.add_markdown_cell("### Classifier : " + "rank " + str(self.rank) + " - number " + str(self.number))
        if self.reshaped:
            self.add_markdown_cell("Reshaping the data of this classifier")
            self.add_code_cell(self.reshaped_code())
        if self.flattened:
            self.add_markdown_cell("Flattening the data of this classifier")
            self.add_code_cell(self.flatten_code())
        self.add_markdown_cell("Creating the model")
        self.add_code_cell(self.create_model_code())
        self.add_markdown_cell("Training and evaluating the model")
        self.add_code_cell(self.train_and_evaluate_model_code())
        return super().get_notebook()
        