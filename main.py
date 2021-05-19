from notifypy import Notify
import uiuc_api as ua
import datetime
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(ua.get_course("CS 173").serialize())
    print_hi('PyCharm')


    notification = Notify()
    notification.title = "Cool Title"
    notification.message = "Even cooler message."
    notification.send()
