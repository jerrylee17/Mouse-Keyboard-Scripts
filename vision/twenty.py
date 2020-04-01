import time
import sys
from playsound import playsound
import threading


def timer(wait=1200):
    for i in range(wait, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "{} minutes {} seconds remaining.".format(i//60, i % 60))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r")


def sound():
    playsound('sound.wav')


def spawnThread(n=5):
    threads = []
    for i in range(n):
        t = threading.Thread(target=sound)
        threads.append(t)
    return threads


def executeThreads(threads, wait=3):
    for t in threads:
        t.start()
        time.sleep(wait)
    for t in threads:
        t.join()


def executeSound(rings=10):
    threads = spawnThread(rings)
    executeThreads(threads, 3)


timer(1)
executeSound()
