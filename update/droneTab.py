from calc.SD import standard_deviation_signal_level
from calc.sumSignalLevel import sum_signal_level
from calc.averageSignalLevel import average_signal_level

def update_drone_tab(parsed_cells):
    global avg_signal_label, sum_signal_label, std_dev_label

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
