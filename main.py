import subprocess
from clearTreeview import clear_treeview
from detectDrone.calc.SD import standard_deviation_signal_level
from detectDrone.calc.averageSignalLevel import average_signal_level
from detectDrone.calc.sumSignalLevel import sum_signal_level
from match import match
from parseCell import parse_cell
from sortCells import sort_cells

interface = "wlan0"
scanning = True
columns = ["Name", "Quality", "Channel", "Encryption", "Address", "Signal"]

def main():
    global tree, avg_signal_label, sum_signal_label, std_dev_label
    cells = [[]]
    parsed_cells = []

    proc = subprocess.Popen(["iwlist", interface, "scan"], stdout=subprocess.PIPE,universal_newlines=True)
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

    if scanning:
        clear_treeview(tree)
        table_data = [list(cell[column] for column in columns) for cell in parsed_cells]
        for row in table_data:
            tree.insert("", "end", values=row)

        avg_signal = average_signal_level(parsed_cells)
        sum_signal = sum_signal_level(parsed_cells)
        std_dev = standard_deviation_signal_level(parsed_cells, avg_signal)
        if avg_signal is not None:
            avg_signal_label.config(text=f"Average signal level: {avg_signal} dBm")
            sum_signal_label.config(text=f"Sum signal level: {sum_signal} dBm")
            std_dev_label.config(text=f"Standard Deviation: {std_dev} dBm")
        else:
            avg_signal_label.config(text="No Wi-Fi networks detected")
            sum_signal_label.config(text="No Wi-Fi networks detected")
            std_dev_label.config(text="No Wi-Fi networks detected")