from queue import Queue
import threading

class InstaViewBot(threading.Thread):
    def __init__(self):
        super(InstaViewBot, self).__init__()
        self.queue = Queue()
        self.setDaemon(True)
        self.threads = []

    def put(self, element):
        self.queue.put(element)

    def wait(self):
        self.queue.join()

    def run(self):
        while True:
            try:
                item = self.queue.get()
                print(f'Working on {item}')
                print(f'Finished {item}')
                self.queue.task_done()
            except Exception:
                self.queue.task_done()


i=InstaViewBot()
i.start()
for item in range(30):
    i.put(item)

i.wait()