import threading
import time

def func1():
    for i in range(10):
        print("This is func1: ", i)
        
def func2():
    for i in range(10):
        print("This is func2: ", i)


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t1.join()  # Wait for t1 to finish before starting t2

t2.start()

# Synchronization using Lock

x = 8192

lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()  # Runs block 
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the Max!")
    lock.release()  # Releases block

def half():
    global x, lock
    lock.acquire()  # Runs block
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the Min!")
    lock.release()  # Releases block

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()


# Semaphore - limits the number of threads that can access a resource

semaphore = threading.BoundedSemaphore(value=5)  # Allow only 5 threads to access the resource

def access(thread_id):
    print(f"Thread {thread_id} is trying to access the resource.")
    semaphore.acquire()  # Acquire the semaphore
    print(f"Thread {thread_id} has accessed the resource.")
    time.sleep(10)  # Simulate some work with the resource
    print(f"Thread {thread_id} is releasing the resource.")
    semaphore.release()  # Release the semaphore

for thread_id in range(1,11):
    t = threading.Thread(target=access, args=(thread_id,))
    t.start()
    time.sleep(1)


# Events - used for signaling between threads

event = threading.Event() # Create an event object to trigger action

def my_func():
    print("Waiting for the event to trigger..")
    event.wait()  # Wait until the event is set
    print("Event has been set! Continuing with the function...")

t1 = threading.Thread(target=my_func)
t1.start()

x = input("Press y to trigger the event...")
if x == 'y':
    event.set()  # Set the event to trigger the waiting thread



# Daemon threads - run in the background and do not prevent the program from exiting

path = "text.txt"
text = ""

def read_file():
    global path, text
    while True:
        with open("text.txt", 'r') as f:
            text = f.read()
        time.sleep(3)  # Check for updates every 3 seconds

def print_text():
    for i in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=print_text)

t1.start()
t2.start()
