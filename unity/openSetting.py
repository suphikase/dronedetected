import config
import tkinter as tk

def open_settings():
    settings_window = tk.Toplevel()
    settings_window.title("Settings")

    tk.Label(settings_window, text="Update Interval (seconds):").grid(row=0, column=0, sticky=tk.W)
    update_interval_var = tk.StringVar()
    update_interval_var.set(config["update_interval"])
    tk.Entry(settings_window, textvariable=update_interval_var).grid(row=0, column=1)

    tk.Label(settings_window, text="Buzzer Pin:").grid(row=1, column=0, sticky=tk.W)
    buzzer_pin_var = tk.StringVar()
    buzzer_pin_var.set(config["buzzer_pin"])
    tk.Entry(settings_window, textvariable=buzzer_pin_var).grid(row=1, column=1)

    def save_and_close():
        global update_interval, buzzer_pin
        config["update_interval"] = int(update_interval_var.get())
        config["buzzer_pin"] = int(buzzer_pin_var.get())
        update_interval = config["update_interval"]
        buzzer_pin = config["buzzer_pin"]
        config.save_config(config)
        settings_window.destroy()

    save_button = tk.Button(settings_window, text="Save", command=save_and_close)
    save_button.grid(row=2, column=0, columnspan=2)

    settings_window.mainloop()