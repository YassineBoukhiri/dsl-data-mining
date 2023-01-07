from SelectorBuilder import SelectorBuilder
from model.App import App


class AppBuilder:
    """
    Builder for the application.
    """

    def __init__(self, name):
        self.name = name
        self.selector = None
        self.transformer = None

    def select_all(self):
        self.selector = SelectorBuilder().select_all()
        return self
    
    def select(self):
        self.selector = SelectorBuilder(self)
        return self.selector
    
    def transform(self):
        self.transformer = TransformerBuilder(self)
        return self.transformer
    
    def build(self):
        app = App(self.name, self.selector.build())
        app.generate()

    def __repr__(self) -> str:
        return App.__repr__(self)

    def __str__(self) -> str:
        return self.__repr__()
