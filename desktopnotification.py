from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(title=" break", message="have a break have a kitkat",timeout=5)
        time.sleep(10)