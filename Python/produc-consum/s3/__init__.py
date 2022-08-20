import time
from threading import Thread, Event
import random

items = []
event = Event()

class Consumer(Thread):

    def __init__(self,event):
        Thread.__init__(self)

        self.event = event

    def run(self):
        global items
        while True:
            time.sleep(2)
            self.event.wait()
            item = items.pop()
            print("poped 1 item from list")

class Producer(Thread):

    def __init__(self, event):
        Thread.__init__(self)

        self.event = event

    def run(self):
        global items
        for i in range(100):

            time.sleep(2)

            item = random.randint(0, 256)
            items.append(item)
            print("items added to list")
            self.event.set()
            self.event.clear()

if __name__ == '__main__':
    consumer, producer =(Consumer(event), Producer(event))

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()