from urllib.request import urlopen as uOpen
from queue import Queue
import core
from thread_class import Worker
from utils import get_url
from time import time

start = time()

f = open('testing.txt', 'w')

last_page = core.get_last_page() 
q = Queue()

for i in range(4):
    worker = Worker(q, f)
    worker.daemon = True
    worker.start()

for x in range(last_page):
    q.put(str(get_url()) + str(x+1))

q.join()

f.close()

print("Took {}".format(time()-start))