from threading import Thread
from time import sleep

"""
Starting a new thread will be processed on the same 
CPU because of the GIL (Global Interpreter Lock).
For separate CPU usage start a new process using 
multiprocessing.  
"""

def threaded_function(arg):
    for i in range(arg):
        print "running"
        sleep(1)

if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    thread.start()
    thread.join()
    print "thread finished...exiting"