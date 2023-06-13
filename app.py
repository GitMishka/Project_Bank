import random
import uuid
from datetime import datetime, timedelta

class BankTransaction:
    def __init__(self):
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type = random.choice(['deposit', 'withdrawal', 'transfer'])
        self.amount = round(random.uniform(1.0, 10000.0), 2)  # Transaction amount in a range of $1.00 to $10,000.00
        self.timestamp = datetime.now() - timedelta(days=random.randint(0, 365))  # Timestamp within the last year
def create_transactions(n):
    return [BankTransaction() for _ in range(n)]
import json

def transaction_to_dict(transaction):
    return {
        'transaction_id': transaction.transaction_id,
        'transaction_type': transaction.transaction_type,
        'amount': transaction.amount,
        'timestamp': transaction.timestamp.isoformat()
    }

def write_transactions_to_file(transactions, filename):
    transactions_dict = [transaction_to_dict(t) for t in transactions]
    with open(filename, 'w') as f:
        json.dump(transactions_dict, f)
transactions = create_transactions(1000)
write_transactions_to_file(transactions, 'transactions.json')
