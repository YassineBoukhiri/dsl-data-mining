import nbformat as nbf

class App:

    def __init__(self, name, selector, transformer, data_miner):
        self.name = name
        self.selector = selector
        self.transformer = transformer
        self.data_miner = data_miner

    def __repr__(self):
        result = "App name : " + self.name + "\n" + self.selector.__repr__() + "\n" + self.transformer.__repr__()
        return result

    def generate(self):
        nb = nbf.v4.new_notebook()
        text = """\
        # My first automatic Jupyter Notebook : """ + self.name + """
        This is an auto-generated notebook."""
        nb['cells'] = [nbf.v4.new_markdown_cell(text)]

        nb['cells'] += self.selector.get_notebook()

        nb['cells'] += self.transformer.get_notebook()

        nb['cells'] += self.data_miner.get_notebook()
    
        fname = 'test.ipynb'

        with open(fname, 'w') as f:
            nbf.write(nb, f)