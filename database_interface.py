import psycopg2

def flush_function(transactions):
    # Set up a connection to your database
    # Replace these values with your actual database parameters
    
    conn = psycopg2.connect(
        dbname="your_database_name", 
        user="your_username", 
        password="your_password", 
        host="localhost"
    )

    # Create a new cursor object
    cur = conn.cursor()

    # Iterate over the transactions and write each one to the database
    for transaction in transactions:
        try:
            # SQL query to insert the transaction into the database
            query = """
            INSERT INTO transactions (transaction_id, transaction_type, amount, timestamp) 
            VALUES (%s, %s, %s, %s)
            """
            data = (transaction.transaction_id, transaction.transaction_type, transaction.amount, transaction.timestamp)
            
            # Execute the SQL command
            cur.execute(query, data)
        
        except Exception as e:
            print(f"Failed to insert transaction {transaction.transaction_id} into the database. Error: {str(e)}")

    # Commit the changes
    conn.commit()

    # Close the database connection
    cur.close()
    conn.close()
