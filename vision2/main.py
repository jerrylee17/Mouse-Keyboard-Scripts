import time
import sys


def timer(wait=1200):
    for i in range(wait, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "{} minutes {} seconds remaining.".format(i//60, i % 60))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r")


# Wait for 20 minutes
timer()
