from queue import Queue
import threading

class InstaViewBot(threading.Thread):
    def __init__(self, queue):
        self.queue = queue
        super(InstaViewBot, self).__init__()
        self.setDaemon(True)
        self.threads = []

    def run(self):
        while True:
            try:
                item = self.queue.get()
                print(f'Working on {item}')
                print(f'Finished {item}')
                self.queue.task_done()
            except Exception:
                self.queue.task_done()


class Test():
    def __init__(self):
        self.queue = Queue()

    def put(self, element):
        self.queue.put(element)

    def wait(self):
        self.queue.join()

    def execute(self):
        self.threads = []
        self.threads.append(InstaViewBot(self.queue))
        self.threads[-1].start()
        self.queue.join()

i = Test()
i.execute()
for item in range(30):
    i.put(item)

i.wait()
