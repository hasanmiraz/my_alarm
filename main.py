import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10,
    )


alert_me = int(input('give minutes: '))
alert_message = input('perpose of the timer: ')
time.sleep(alert_me*60)
send_notification(f"Time Check: {alert_me} min",f"{alert_message}")
