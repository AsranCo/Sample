import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)


class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        for i in range(5):
            if not q.full():
                q.put(i)
                logging.debug('Putting ' + str(i)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        logging.debug("Putting items in queue finish!")


class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        logging.debug("Queue in empty!")


if __name__ == '__main__':

    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(4)
    c.start()
    time.sleep(2)
