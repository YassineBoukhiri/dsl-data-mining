import nbformat as nbf

class App:

    def __init__(self, name, selector, preprocessor, transformer, data_miner, comparator):
        self.name = name
        self.selector = selector
        self.preprocessor = preprocessor
        self.transformer = transformer
        self.data_miner = data_miner
        self.comparator = comparator

    def __repr__(self):
        result = "App name : " + self.name + "\n" + self.selector.__repr__() + "\n" + self.transformer.__repr__()
        return result

    def generate(self):
        nb = nbf.v4.new_notebook()
        text = \
        """# My first automatic Jupyter Notebook : """ + self.name + """\n""" + \
        """This is an auto-generated notebook."""
        nb['cells'] = [nbf.v4.new_markdown_cell(text)]

        nb['cells'] += self.selector.get_notebook()

        nb['cells'] += self.preprocessor.get_notebook()

        nb['cells'] += self.transformer.get_notebook()

        nb['cells'] += self.data_miner.get_notebook()

        nb['cells'] += self.comparator.get_notebook()
    
        fname = 'test.ipynb'

        with open(fname, 'w') as f:
            nbf.write(nb, f)