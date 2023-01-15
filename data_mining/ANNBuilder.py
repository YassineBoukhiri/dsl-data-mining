from ClassifierBuilder import ClassifierBuilder


class ANNBuilder(ClassifierBuilder):
    """
    Builder for the ANNBuilder.
    """

    def __init__(self, root, number):
        super().__init__(root, number)
        self.root = root
    

    def build(self):
        return super().build()
    

