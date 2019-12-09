# Threading

import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(7):
            print(threading.currentThread().getName())

x = BuckysMessenger(name = "Send out messages") # thread is responsible for
y = BuckysMessenger(name = "recevie messages") # thread is responsible for

x.start()
y.start()

# Both of these are running at the same time (synchronization)