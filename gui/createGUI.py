import threading
import tkinter as tk
import tkinter.ttk as ttk
from calc.SD import standard_deviation_signal_level
from calc.averageSignalLevel import average_signal_level
from calc.sumSignalLevel import sum_signal_level
from clearTreeview import clear_treeview
from detectDrone.main import main
from detectDrone.reset import reset
from detectDrone.update.wifiData import update_wifi_data
from gui.createTable import create_table
from logAlert import log_alert
from openSetting import open_settings
from playBuzzerAlarm import play_buzzer_alarm
from toggleLogging import toggle_logging
from update.wifiTab import columns


tree = None  
def create_gui(parsed_cells):
    global avg_signal_label, sum_signal_label, std_dev_label
    
    root = tk.Tk()
    root.geometry('1200x900')
    root.maxsize(1200,900)
    root.minsize(1200,900)
    root.title("Wi-Fi Networks")

    logo = tk.PhotoImage(file="/home/admin/Desktop/code_scan/LOGOV3.png")
    logo_label = tk.Label(root,image=logo)
    logo_label.pack(side=tk.TOP, anchor=tk.W)
    global tab_parent, wifi_tab
    tab_parent = ttk.Notebook(root)
    wifi_tab = ttk.Frame(tab_parent,width=400, height=700)

    drone_tab = ttk.Frame(tab_parent,width=400, height=700)
    
    wifi_tab.pack(expand=True, fill=tk.BOTH)
    drone_tab.pack(expand=True, fill=tk.BOTH)

    tab_parent.add(wifi_tab, text="Wi-Fi Networks")
    tab_parent.add(drone_tab, text="Drone Detector")

    table_data = [list(cell[column] for column in columns) for cell in parsed_cells]
    create_table(wifi_tab, table_data)

    avg_signal = average_signal_level(parsed_cells)
    sum_signal = sum_signal_level(parsed_cells)
    std_dev = standard_deviation_signal_level(parsed_cells, avg_signal)
    avg_signal_label = tk.Label(drone_tab, text=f"Average signal level: {avg_signal} dBm",font=('Times',24))
    sum_signal_label = tk.Label(drone_tab, text=f"Sum signal level: {sum_signal} dBm",font=('Times',24))
    std_dev_label = tk.Label(drone_tab, text=f"Standard Deviation: {std_dev} dBm",font=('Times',24))  
    
    threshold = -60  
    if avg_signal is not None and avg_signal >= threshold * 0.9:
        play_buzzer_alarm()
        log_alert(avg_signal)
        detected_label = tk.Label(drone_tab, text="\n\nDrone Detected!\n",font=('Times',40),fg="red")
        detected_label.pack()

    avg_signal_label.pack()
    sum_signal_label.pack()
    std_dev_label.pack()

    global logging_enabled
    logging_enabled = tk.BooleanVar()
    logging_enabled.set(True)
    logging_checkbox = tk.Checkbutton(drone_tab, text="Enable logging", variable=logging_enabled, command=toggle_logging,font=('Times',20))
    logging_checkbox.pack()
    
    on_img = tk.PhotoImage(file='/home/admin/Desktop/code_scan/on4.png')
    off_img = tk.PhotoImage(file='/home/admin/Desktop/code_scan/off4.png')
    setting_img = tk.PhotoImage(file='/home/admin/Desktop/code_scan/setting2.png')
    
    def toggle_scan():
        global scanning
        scanning = not scanning

        if scanning:
            on_off_button.config(image=on_img)
            main()
        
        else:
            on_off_button.config(image=off_img)
            clear_treeview(tree)
    
    on_off_button = tk.Button(root, image=on_img,relief='flat' ,command=lambda: toggle_scan())
    on_off_button.place(x=700, y=100)
    
    settings_button = tk.Button(root, image=setting_img,relief='flat', command=open_settings())
    settings_button.place(x=900, y=100)

    reset_button = tk.Button(root, text='Reset', command=reset)     ##################################
    reset_button.place(x=1100, y=100)

    tab_parent.pack(expand=True, fill=tk.BOTH)
    
    update_thread = threading.Thread(target=update_wifi_data)
    update_thread.start()
    root.mainloop()