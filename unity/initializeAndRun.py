from sqlite3 import InterfaceError
import subprocess
from match import match
from parseCell import parse_cell
from sortCells import sort_cells
from gui.createGUI import create_gui


def initialize_and_run():
    global tree, avg_signal_label, sum_signal_label

    cells = [[]]
    parsed_cells = []

    proc = subprocess.Popen(["iwlist", InterfaceError, "scan"], stdout=subprocess.PIPE, universal_newlines=True)
    out, err = proc.communicate()

    for line in out.split("\n"):
        cell_line = match(line, "Cell ")
        if cell_line is not None:
            cells.append([])
            line = cell_line[-27:]
        cells[-1].append(line.rstrip())

    cells = cells[1:]

    for cell in cells:
        parsed_cells.append(parse_cell(cell))

    sort_cells(parsed_cells)
    create_gui(parsed_cells)