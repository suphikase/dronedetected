import time
from asyncio import subprocess
from sqlite3 import InterfaceError
from unity.match import match
from unity.parseCell import parse_cell
from unity.sortCells import sort_cells
from wifiTab import update_wifi_tab
from droneTab import update_drone_tab
from unity.openSetting import update_interval

def update_wifi_data():
    global tree, avg_signal_label, sum_signal_label, scanning
    
    while scanning:
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
        update_wifi_tab(parsed_cells)
        update_drone_tab(parsed_cells)
        time.sleep(update_interval)