import threading
import time

def operacaomaneira(id):
    time.sleep(0.5)
    print("thread #", id)

def main():
    args = [0] * 5

    for i in range(5):
        args[i] = i + 1

    threads = []

    for i in range (5):
        t = threading.Thread(target=operacaomaneira, args=(args[i],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

main()
