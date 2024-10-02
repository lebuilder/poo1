import threading
import time
import os

class Print(threading.Thread):
    def __init__(self, msg, lock):
        threading.Thread.__init__(self)
        self.__msg = msg
        self.__lock = lock

    def run(self) -> None:
        with self.__lock:
            for car in self.__msg:
                print(car, end="")
                time.sleep(0.01)
            print()

if __name__ == '__main__':
    lock = threading.Lock()
    P1 = Print("bien le bonjour mes amis", lock)
    P2 = Print("il est grand temps de se synchroniser ...", lock)
    os.system("clear")
    P1.start()
    P2.start()
    P1.join()
    P2.join()