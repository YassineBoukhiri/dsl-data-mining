from model.Notebookable import Notebookable

class Deployer(Notebookable):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def get_best_model_code(self) -> str:
        return """best_model = None\
        \nbest_accuracy = 0\
        \nfor key, value in models_metrics.items():\
            \n\taccuracy = value[1][1]\
            \n\tif accuracy > best_accuracy:\
                \n\t\tbest_accuracy = accuracy\
                \n\t\tbest_model = value[2]\
        \nprint(f"Best model accuracy: {best_accuracy}")"""

    def get_saving_model_code(self) -> str:
        return """best_model.save("../prediction-app/model/model.h5")\
        \nprint("The best model has been saved in the directory ../prediction-app/model/model.h5")"""

    def get_naming_app_code(self) -> str:
        return """with open("../prediction-app/.env", "w") as file:\
        \n\tfile.write("APP_NAME=\\\""""+self.name+"""\\\"")"""

    def get_notebook(self) -> str:
        self.add_markdown_cell("""## Deploying the best model""")
        self.add_markdown_cell("""### Finding the best model according to the accuracy""")
        self.add_code_cell(self.get_best_model_code())
        self.add_markdown_cell("""### Saving the best model""")
        self.add_code_cell(self.get_saving_model_code())
        self.add_markdown_cell("""### Setting the name of the application""")
        self.add_code_cell(self.get_naming_app_code())
        self.add_markdown_cell("""### Instructions for running the application""")
        self.add_markdown_cell("""1. Open the terminal and go to the directory ../prediction-app""")
        self.add_markdown_cell("""2. Run the command: steamlit run app.py""")
        self.add_markdown_cell("""3. Open the browser and go to the address: http://localhost:8501""")
        return super().get_notebook()