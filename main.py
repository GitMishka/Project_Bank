from transaction import BankTransaction
from transaction_buffer import TransactionBuffer
from database_interface import flush_function

buffer = TransactionBuffer(3600, flush_function)  # flush every hour

for _ in range(1000):
    transaction = BankTransaction()
    buffer.add_transaction(transaction)
