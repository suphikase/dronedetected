import RPi.GPIO as GPIO

def reset_buzzer():
    global buzzer_pin
    GPIO.output(buzzer_pin, GPIO.LOW)