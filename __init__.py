import RPi.GPIO as GPIO
import initializeAndRun
import config

interface = "wlan0"

tab_parent = None
wifi_tab = None
detected_label = None
buzzer_pin = config["buzzer_pin"]
logging_enabled = config["logging_enabled"]
update_interval = config["update_interval"]

# Set up the buzzer GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

initializeAndRun.initialize_and_run()
