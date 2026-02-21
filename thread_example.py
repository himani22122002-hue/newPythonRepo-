import threading

def task():
    print("Task is running")

# Create threads
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Done")

import threading
import time

def task(name):
    for i in range(3):
        print(f"{name} is running")
        time.sleep(2)

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished")
#How to Prove It’s Not True Parallel?
# Trick: Use CPU-heavy task
import threading

def task():
    x = 0
    for i in range(10**7):
        x += 1
    print("Done")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
#Real Proof Method (Interview Level 🔥)
#Compare time
import threading
import time

def task():
    for i in range(10**7):
        pass

start = time.time()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print("Start:", start)
print("End:", end)
print("Time:", end - start)
