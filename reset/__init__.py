import time
from detectDrone.main import main
from detectDrone.reset.buzzer import reset_buzzer
from detectDrone.reset.data import reset_data
from detectDrone.reset.gui import reset_gui

def reset():
    reset_data()
    reset_buzzer()
    reset_gui()

    time.sleep(1)

    global scanning
    scanning = True
    main()