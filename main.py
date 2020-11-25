# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def count():
    start_time = datetime.datetime.now()
    for i in range(0, 10):
        if i == 10:
            print("counting at: " + str(i))
            print("Done counting...")
        else:
            print("counting at: " + str(i))
            time.sleep(5)  # sleep for 5 seconds
    end_time = datetime.datetime.now()
    print(start_time.time())
    print(end_time.time())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
