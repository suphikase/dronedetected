import config as cf
import RPi.GPIO as GPIO
import time

buzzer_pin = cf["buzzer_pin"]

def play_buzzer_alarm():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzer_pin, GPIO.LOW)