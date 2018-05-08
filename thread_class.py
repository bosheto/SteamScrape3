
from threading import Thread
from core import scrape, connect
from urllib.request import urlopen as uOpen

class Worker(Thread):
    
    def __init__(self,queue, file_write):
        Thread.__init__(self)
        self.file_write = file_write
        self.queue = queue
    
    def run(self):
        while True:
            url = self.queue.get()
            html_source = connect(url)
            scrape(html_source,self.file_write)
            self.queue.task_done()


