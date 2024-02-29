import queue
import time

request_queue = queue.Queue()
request_counter = 0


def generate_requests():
    global request_counter
    new_request = request_counter
    request_queue.put(new_request)
    print(f"Application is added: {new_request}")
    request_counter += 1


def process_requests():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Application is processed: {request}")
    else:
        print("Queue is empty")
        time.sleep(1)


try:
    while True:
        generate_requests()
        time.sleep(1)
        process_requests()
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted by user")
