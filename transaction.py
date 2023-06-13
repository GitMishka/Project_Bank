import random
import uuid
from datetime import datetime, timedelta

class BankTransaction:
    def __init__(self):
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type = random.choice(['deposit', 'withdrawal', 'transfer'])
        self.amount = round(random.uniform(1.0, 10000.0), 2)  
        self.timestamp = datetime.now() - timedelta(days=random.randint(0, 365)) 
