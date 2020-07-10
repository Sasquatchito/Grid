import sys
from PyQt5.QtWidgets import *
from src.Cell import cell 
from src.Grid import grid
from src.Maze import maze


class SudokuWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        grid_layout.setColumnMinimumWidth(0,0)
        self.setLayout(grid_layout)
        self.setWindowTitle('Basic Grid Layout')
        self.g = grid(cell(0))
        self.build_grid()
    def build_grid(self):
        self.g.build_grid(9, 9)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = SudokuWindow()
    #windowExample.show()
    sys.exit(app.exec_())