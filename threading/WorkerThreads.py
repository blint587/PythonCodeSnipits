import threading
import queue
import traceback



nthread = 2 # the number of threads

queueLock = threading.Lock()
workQueue = queue.Queue() # Queue holding "tasks"

threads = []  #thread holder

threadID = 0

projects = ["on", "two", "thre"] # tasks to perform

exitFlag = False


class myThread (threading.Thread):  # thread class
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    def run(self):
        process_data(self.threadID, self.q)  # global scoop function not that good :/

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()  # acquiring lock so only on thread can process on data
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            try:
                print(str(threadName) + str(data))  ## Worker function implementation
            except Exception as z:
                a = traceback.format_exc()
                print(a)
                raise z
        else:
            queueLock.release()

if __name__ == "__main__": # to prevent "ghost threads"
    try:
        for threadID in range(nthread):
            thread = myThread(threadID, workQueue)
            thread.start() #threads are started, but waiting from tasks
            threads.append(thread)

        # Fill the queue
        queueLock.acquire()
        for task in projects:
            workQueue.put(task)
        queueLock.release()

        # Wait for queue to empty
        while not workQueue.empty():
            pass

        # Notify threads it""s time to exit
        exitFlag = True

        # Wait for all threads to complete
        for t in threads:
            t.join()

    except Exception as ex:
        a = traceback.format_exc()
        print(a)
        raise ex