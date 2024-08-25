from threading import Thread
import time

def my_func(i):
    print('Starting thread %d' %i)
    time.sleep(5)
    print('Finishing thread %d ' %i)

for i in range(10):
    t = Thread(target=my_func, args=(i,))
    t.start()
