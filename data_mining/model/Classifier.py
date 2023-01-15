from model.Notebookable import Notebookable
from model.Layer import Layer

class Classifier(Notebookable):

    def __init__(self, rank, number):
        super().__init__()
        self.name = "Classifier"
        self.rank = rank
        self.number = number
        self.layers = []

    def add_layer(self, layer: Layer):
        self.layers.append(layer)

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
        result += "\nprint(\"Accuracy : \", score[1])"
        return result

    def plot_accuracy_and_loss_code(self):
        result = "# summarize history for accuracy" \
                + "\nplt.plot(history.history['accuracy'])" \
                + "\nplt.title('model accuracy')" \
                + "\nplt.ylabel('accuracy')" \
                + "\nplt.xlabel('epoch')" \
                + "\nplt.legend(['train', 'test'], loc='upper left')" \
                + "\nplt.show()" \
                + "\n# summarize history for loss" \
                + "\nplt.plot(history.history['loss'])" \
                + "\nplt.title('model loss')" \
                + "\nplt.ylabel('loss')" \
                + "\nplt.xlabel('epoch')" \
                + "\nplt.legend(['train', 'test'], loc='upper left')" \
                + "\nplt.show()"
        return result

    def get_notebook(self) -> str:
        self.add_markdown_cell("### Classifier : " + "rank " + str(self.rank) + " - number " + str(self.number))
        self.add_markdown_cell("Creating the model")
        self.add_code_cell(self.create_model_code())
        self.add_markdown_cell("Training and evaluating the model")
        self.add_code_cell(self.train_and_evaluate_model_code())
        self.add_markdown_cell("Plotting the accuracy and loss")
        self.add_code_cell(self.plot_accuracy_and_loss_code())
        return super().get_notebook()
        