import nbformat as nbf
from model.Cell import Cell
from model.Cell import CELL_TYPE

class Notebookable:
    def __init__(self):
        self.cells: list[Cell] = []
        self.cells_count = 0
    
    def add_cell(self, cell_type: CELL_TYPE, content: str):
        self.cells_count += 1
        cell = Cell(self.cells_count, cell_type, content)
        self.cells.append(cell)

    def add_code_cell(self, content: str):
        self.add_cell(CELL_TYPE.CODE, content)

    def add_markdown_cell(self, content: str):
        self.add_cell(CELL_TYPE.MARKDOWN, content)
    
    def get_cells(self) -> list[Cell]:
        return self.cells

    def get_notebook(self) -> str:
        notebook = []
        for cell in self.cells:
            if cell.cell_type == CELL_TYPE.CODE:
                notebook.append(nbf.v4.new_code_cell(cell.content))
            elif cell.cell_type == CELL_TYPE.MARKDOWN:
                notebook.append(nbf.v4.new_markdown_cell(cell.content))
        return notebook