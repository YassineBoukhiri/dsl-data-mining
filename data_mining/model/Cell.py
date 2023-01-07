from enum import Enum

class CELL_TYPE(Enum):
    CODE = 1
    MARKDOWN = 2

class Cell: 
    def __init__(self, order: int, cell_type: CELL_TYPE, content: str):
        self.order = order
        self.cell_type = cell_type
        self.content = content