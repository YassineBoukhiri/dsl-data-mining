from model.Notebookable import Notebookable
from model.ComparisonParameter import ComparisonParameter

class Comparator(Notebookable):

    def __init__(self):
        super().__init__()
        self.metrics = []
        self.parameters = []

    def get_parameter_by_name(self, name: str) -> ComparisonParameter:
        for parameter in self.parameters:
            if parameter.name == name:
                return parameter
        return None

    def code_plotting_metrics(self):
        result = ""
        for metric in self.metrics:
            result += self.code_plot_metric(metric)
        return result

    def code_parameters(self):
        result = ""
        for i,parameter in enumerate(self.parameters):
            result += str(parameter) + " and " if i < len(self.parameters) - 1 else str(parameter)
        return result

    def code_plot_metric(self, metric: str):
        result = "# Plot " + metric + " of the classifiers"
        result += "\nfor key, value in models_metrics.items():"
        if self.parameters == []:
            result +=   "\n\thistory = value[0]"
            result +=   "\n\tplt.plot(history.history['" + metric + "'])"
        else:
            result +=   "\n\tif " + self.code_parameters() + ":"
            result +=       "\n\t\thistory = value[0]"
            result +=       "\n\t\tplt.plot(history.history['" + metric + "'])"
        result += "\nplt.title('model " + metric + "')"
        result += "\nplt.ylabel('" + metric + "')"
        result += "\nplt.xlabel('epoch')"
        result += "\nplt.legend(models_metrics.keys(), loc='upper left')"
        result += "\nplt.show()"
        return result

    def get_notebook(self) -> str:
        self.add_markdown_cell("""## Comparison of classifiers""")
        self.add_markdown_cell("""### Importing libraries""")
        self.add_code_cell("""import matplotlib.pyplot as plt""")
        self.add_markdown_cell("""### Plotting the metrics""")
        for metric in self.metrics:
            self.add_markdown_cell("#### Plot of the " + metric)
            self.add_code_cell(self.code_plot_metric(metric))
        return super().get_notebook()