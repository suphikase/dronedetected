def reset_data():
    global logging_enabled
    if logging_enabled:
        with open("/home/admin/Desktop/wifi_alert_log.txt", "a") as log_file:
            log_file.write("Reset data\n")