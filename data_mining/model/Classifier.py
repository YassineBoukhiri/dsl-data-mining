from model.Notebookable import Notebookable

class Classifier(Notebookable):

    def __init__(self):
        super().__init__()
        self.name = "Classifier"
        self.layers = []

    def add_dense_layer(self, nb_neurons, activation=None):
        if activation is None:
            activation = "relu"
        if len(self.layers) == 0:
            self.layers.append("Dense(" + str(nb_neurons) + ", activation=\"" + str(activation) + "\", input_shape=(X_train.shape[1],))")
        else:
            self.layers.append("Dense(" + str(nb_neurons) + ", activation=\"" + str(activation) + "\")")

    def create_model_code(self):
        result = "model = Sequential()"
        for layer in self.layers:
            result += "\nmodel.add(" + layer + ")"
        result += "\nmodel.compile(optimizer=\"adam\", loss=\"sparse_categorical_crossentropy\", metrics=[\"accuracy\"])"
        result += "\nmodel.summary()"
        return result

    def train_and_evaluate_model_code(self):
        result = "model.fit(X_train, Y_train)"
        result += "\nscore = model.evaluate(X_test, Y_test)"
        result += "\nprint(\"Accuracy : \", score[1])"
        return result



    def get_notebook(self) -> str:
        self.add_markdown_cell("### Classifier : " + self.name)
        self.add_markdown_cell("Creating the model")
        self.add_code_cell(self.create_model_code())
        self.add_markdown_cell("Training and evaluating the model")
        self.add_code_cell(self.train_and_evaluate_model_code())
        return super().get_notebook()
        