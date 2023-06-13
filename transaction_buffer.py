import threading
import queue
import time
from datetime import datetime

class TransactionBuffer:
    def __init__(self, flush_frequency_in_seconds, flush_function):
        self.buffer = queue.Queue()  # Thread-safe queue
        self.flush_frequency = flush_frequency_in_seconds
        self.flush_function = flush_function
        self.last_flush = datetime.now()
        self.start_background_flush()

    def add_transaction(self, transaction):
        self.buffer.put(transaction)

    def start_background_flush(self):
        def run():
            while True:
                time.sleep(self.flush_frequency)
                self.flush()
        
        thread = threading.Thread(target=run)
        thread.start()

    def flush(self):
        transactions_to_flush = []
        while not self.buffer.empty():
            transactions_to_flush.append(self.buffer.get())

        try:
            self.flush_function(transactions_to_flush)
            self.last_flush = datetime.now()
        except Exception as e:
            print(f"Flush failed at {self.last_flush} with error {str(e)}. Re-queueing transactions.")
            for transaction in transactions_to_flush:
                self.buffer.put(transaction)
