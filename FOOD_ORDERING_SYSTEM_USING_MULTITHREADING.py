""" 1). Design a food ordering system where your python program will run two threads,

        i). Place Order: This thread will be placing an order and inserting that into a queue.
        This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)

        ii).Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it.
         This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
"""

import time
import threading
from collections import deque


class queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop()

    def show_queue(self):
        return self.queue


order_placed = queue()


def place_order():
    for order in orders:
        print(f"PLACing YOUr ORDER: {order}")
        order_placed.enqueue(order)
        time.sleep(0.5)
    print("-" * 60)


def srve_order():
    time.sleep(1)
    for i in range(len(orders)):
        print(f"SERVING YOUR ORDER: {orders[i]}")
        order_placed.dequeue()
        time.sleep(2)


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

t = time.time()
t1 = threading.Thread(target=place_order)
print("-" * 60)
t2 = threading.Thread(target=srve_order)

t1.start()
t2.start()

t1.join()
t2.join()

print("-" * 49)
print(f"THE TIME {round(time.time() - t)}.sec TAKEN TO SERVE THE ORDER((($)))")
print("-" * 49)
