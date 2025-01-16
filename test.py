import _thread
import time

# A simple function that simulates a task running in a thread
def task_1():
    while True:
        print("Task 1 is running")
        time.sleep(1)

def task_2():
    while True:
        print("Task 2 is running")
        time.sleep(1.5)

# Create two threads
_thread.start_new_thread(task_1, ())
_thread.start_new_thread(task_2, ())

# Main loop that keeps the program running
while True:
    print("Main thread is running")
    time.sleep(2)
