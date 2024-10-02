import threading
import time
import os

class Print(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.__msg = msg

    def run(self) -> None:
        for car in self.__msg:
            print(car, end="")
            time.sleep(0.01)
        print()

if __name__ == '__main__':
    P1 = Print("bien le bonjour mes amis")
    P2 = Print("il est grand temps de se synchroniser ...")
    os.system("clear")
    P1.start()
    P1.join()  
    P2.start()
    P2.join()  