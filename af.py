import time


def wait_for_completion(callback):
    time.sleep(2)
    callback()


def log_completion():
    print("complete")


wait_for_completion(callback=log_completion)

wait_for_completion(callback=lambda: print("complete"))
