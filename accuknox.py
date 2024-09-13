import time
import threading

"""
Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized. We can iterate over an
instance of the Rectangle class When an instance of the Rectangle class is iterated over, we first get its length in
the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

"""


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.which_side = 0

    def __iter__(self):
        self.which_side = 0
        return self

    def __next__(self):
        if self.which_side == 0:
            self.which_side += 1
            return {"length": self.length}
        elif self.which_side == 1:
            self.which_side += 1
            return {"width": self.width}
        else:
            raise StopIteration


rectangle = Rectangle(10, 5)

for side in rectangle:
    print(side)

print("-" * 15)
print("Topic: Django Signals")
"""
Topic: Django Signals
        I've only worked with Flask, so I'll answer based on my understanding of how things work in Flask.

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a 
code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, 
we just need to understand your logic.
Answer: Synchronously
    Logic: Django's signals might work similarly to Flask's event listeners. In Flask, signals are synchronous unless we
    explicitly handle them in asynchronous manner. e.g.: threads. Based on that understanding, I would assume that
    Django's signals are executed synchronously by default.
"""


def signal_handler_q1():
    print("Signal received")
    print("Waiting . . .")
    time.sleep(2)
    print("Signal handled")


def main_q1():
    print("Sending signal")
    signal_handler_q1()  # This is synchronous
    print("Signal sent")


print("-" * 15)
print("Question 1")
main_q1()

"""
Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet 
that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to 
understand your logic.
Answer: Yes it would run in the same thread as the caller.
    Logic: From a Flask perspective, where signals are typically run in the same thread as the caller, I’d assume
    Django’s signals operate similarly. If Flask signals were running in a different thread, we would usually need to
    handle them with explicit threading which would be different from the default synchronous behavior.
"""


def signal_handler_q2():
    print(f"Signal received in thread: {threading.current_thread().name}")
    print("Waiting . . .")
    time.sleep(2)
    print(f"Signal handled in thread: {threading.current_thread().name}")


def main_q2():
    print(f"Main thread: {threading.current_thread().name}")
    signal_handler_q2()  # This runs in the same thread
    print(f"After signal in thread: {threading.current_thread().name}")


print("-" * 15)
print("Question 2")
main_q2()

"""
Question 3: By default do django signals run in the same database transaction as the caller? Please support your 
answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production 
ready, we just need to understand your logic.
Answer: Yes it would run in the same transaction as the caller.
    Logic: From a Flask perspective, where custom hooks or signals typically operate within the same context (like a 
    database transaction) unless explicitly handled otherwise, I’d infer that Django’s signals also run in the same 
    database transaction by default. In Flask, database transactions are usually handled synchronously in the same 
    context, so it’s reasonable to assume Django follows a similar pattern.
"""


class TransactionContext:
    def __init__(self):
        self.transaction_id = None

    def start_transaction(self):
        self.transaction_id = "transaction_1"

    def end_transaction(self):
        print(f"Transaction ended: {self.transaction_id}")


def signal_handler_q3(context):
    print(f"Signal received in transaction: {context.transaction_id}")
    print("Waiting . . .")
    time.sleep(2)
    print(f"Signal handled in transaction: {context.transaction_id}")


def main_q3():
    context = TransactionContext()
    context.start_transaction()
    print(f"Main transaction: {context.transaction_id}")
    signal_handler_q3(context)  # This runs within the same transaction
    context.end_transaction()


print("-" * 15)
print("Question 3")
main_q3()
