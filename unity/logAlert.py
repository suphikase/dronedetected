import datetime as D

def log_alert(average_signal):
    global logging_enabled
    if logging_enabled:
        timestamp = D.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - Alert & Detected: Average signal level: {average_signal} dBm\n"

        with open("/home/admin/Desktop/wifi_alert_log.txt", "a") as log_file:
            log_file.write(log_entry)