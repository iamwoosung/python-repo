import time
from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

if __name__ == "__main__":
    start = time.time()
    
    START, END = 0, 100000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END, result))
    
    th1.start()
    
    th1.join()
    

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp

    print(f"Result: {total}")
    print(f"Time: { time.time() - start }")