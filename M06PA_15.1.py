import multiprocessing
import random
from datetime import datetime
from time import sleep

def worker(seconds):
    #random number of seconds between 0 - 1
    sleep(seconds)
    # Display
    print('Current time is ', datetime.utcnow(), 'after waiting', seconds, 'seconds')
    
if __name__ == "__main__":
    #List to keep track of processes
    processes = []

#Create and start processes
    for n in range(3):
        seconds = random.random()
        time_process = multiprocessing.Process(target=worker, args=(seconds,))
        processes.append(time_process)
        time_process.start()

#wait for all processes to finish
    for p in processes:
        p.join()