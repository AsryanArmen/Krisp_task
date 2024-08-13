import io
from collections import deque

# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)`
    for each payment.
    Returns when there are no more payments.
    """
    # Sample implementation to make the code run in coderpad.
    # In a real scenario, this function would interact with a payment processor.
    for i in range(10):
        callback_fn(i)

# This is a library function, you can't modify it.
def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator
    and stores them to a remote system.
    """
    # Sample implementation to make the code run in coderpad.
    # In a real scenario, this function would store payments to a remote system.
    for i in amount_iterator:
        print(i)

def callback_example(amount):
    print(amount)
    return True

def process_payments_2():
    # Initialize a deque (double-ended queue) to store payment amounts temporarily.
    queue = deque()

    # This is the callback function that will be passed to `stream_payments()`.
    # It will be called for each payment, adding the payment amount to the queue.
    def callback(amount):
        # Add the payment amount to the queue.
        queue.append(amount)

    # This generator function will be passed to `store_payments()`.
    # It will yield payments from the queue one by one to be stored.
    def payment_generator():
        # Infinite loop to continuously check the queue for new payments.
        while True:
            # While there are payments in the queue, yield them one by one.
            while queue:
                yield queue.popleft()  # Pop and yield the leftmost item from the queue.
            # If the queue is empty, break the loop to stop the generator.
            if not queue:
                break

    # Start the payment streaming process.
    # This will call the `callback` function for each payment.
    stream_payments(callback)

    # Start the payment storing process.
    # This will consume payments from the `payment_generator` and store them.
    store_payments(payment_generator())

# Run the payment processing function.
process_payments_2()
