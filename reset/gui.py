from clearTreeview import clear_treeview
from detectDrone.reset.buzzer import reset_buzzer
from detectDrone.reset.data import reset_data


def reset_gui():
    global tree, avg_signal_label, sum_signal_label, std_dev_label, detected_label
    
    reset_data()
    reset_buzzer()
    
    avg_signal_label.config(text=f"Average signal level: 0 dBm")
    sum_signal_label.config(text=f"Sum signal level: 0 dBm")
    std_dev_label.config(text=f"Standard Deviation: 0 dBm")
    if detected_label is not None:
       detected_label.config(text="")
    clear_treeview(tree)