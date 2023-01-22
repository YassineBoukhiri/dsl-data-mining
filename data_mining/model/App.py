import nbformat as nbf
import datetime

class App:

    def __init__(self, name, selector, preprocessor, transformer, data_miner, comparator, deployer):
        self.name = name
        self.selector = selector
        self.preprocessor = preprocessor
        self.transformer = transformer
        self.data_miner = data_miner
        self.comparator = comparator
        self.deployer = deployer

    def __repr__(self):
        result = "App name : " + self.name + "\n" + self.selector.__repr__() + "\n" + self.transformer.__repr__()
        return result

    def generate(self):
        nb = nbf.v4.new_notebook()
        text = \
        """# Automatic Jupyter Notebook : """ + self.name + """\n""" + \
        """This is an auto-generated notebook generated using the classifAI DSL on : """ + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
        nb['cells'] = [nbf.v4.new_markdown_cell(text)]

        nb['cells'] += self.selector.get_notebook()

        if self.preprocessor is not None:
            nb['cells'] += self.preprocessor.get_notebook()

        if self.transformer is not None:
            nb['cells'] += self.transformer.get_notebook()

        nb['cells'] += self.data_miner.get_notebook()

        if self.comparator is not None:
            nb['cells'] += self.comparator.get_notebook()

        if self.deployer is not None:
            nb['cells'] += self.deployer.get_notebook()
    
        fname = 'notebook.ipynb'

        with open(fname, 'w') as f:
            nbf.write(nb, f)