import multiprocessing
import time 
t = time.time()
numbers = [1,2,3,4]
def sqaure(numbers):
    for number in numbers:
        lock.acquire()
        print('square:', number * number)
        time.sleep(1)
        lock.release()
        

def cube(numbers):
    for number in numbers:
        lock.acquire()
        print('cube:', number * number * number)
        time.sleep(1)
        lock.release()

p1 = multiprocessing.Process(target = sqaure, args=(numbers,) )
p2 = multiprocessing.Process(target = cube, args=(numbers,) )
lock = multiprocessing.Lock()

p1.start()
p2.start()

p1.join()
p2.join()

print('Done!')
print(time.time() - t)
