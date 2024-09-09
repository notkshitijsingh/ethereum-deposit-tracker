# importing necessary modules
from web3 import Web3
import sqlite3
import time
import logging
import os

# setting up a logging file
log_file = 'tracker.log'
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# confirming existence of log file
if os.path.exists(log_file):
    print(f"Log file '{log_file}' created successfully.")
else:
    print(f"Failed to create log file '{log_file}'.")

# connecting to ethereum node using 'alchemy' as recommended
provider_url = 'https://eth-mainnet.g.alchemy.com/v2/8PNv36Fl447desrrVXP2yqYDw3UWmgCc'
w3 = Web3(Web3.HTTPProvider(provider_url))

# checking connection
if w3.is_connected():
    logging.info("Connected to Ethereum Node")
    print("Connected to Ethereum Node")
else:
    logging.error("Connection Failed")
    print("Connection Failed")
    exit(1)

# beacon deposit contract address (lowercase for consitency)
contract_address = '0x00000000219ab540356cbb839cbe05303d7705fa'.lower() 

# setup sqlite database
def init_db():
    try:
        conn = sqlite3.connect('deposits.db')
        cursor = conn.cursor()
        # create the deposits table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS deposits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                blockNumber INTEGER,
                blockTimestamp INTEGER,
                sender TEXT,
                amount REAL,
                hash TEXT UNIQUE
            )
        ''')
        conn.commit()
        return conn, cursor
    except Exception as e:
        logging.error(f"Error initializing database: {e}")
        print(f"Error initializing database: {e}")
        return None, None

# inserting deposit data into the database
def save_deposit(deposit_data, cursor, conn):
    try:
        # ensure 'sender' is a string and 'amount' is converted from decimal to float
        # since sqlite doesn't support decimal by default
        cursor.execute('''
            INSERT INTO deposits (blockNumber, blockTimestamp, sender, amount, hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            deposit_data['blockNumber'],
            deposit_data['blockTimestamp'],
            str(deposit_data['sender']),  # ensure the address is stored as string
            float(deposit_data['amount']),  # convert Decimal to float
            deposit_data['hash']
        ))
        conn.commit()
        logging.info(f"Saved deposit: {deposit_data}")
        print(f"Saved deposit: {deposit_data}")
    except sqlite3.IntegrityError:
        logging.warning(f"Duplicate entry found for transaction {deposit_data['hash']}")
        print(f"Duplicate entry found for transaction {deposit_data['hash']}")
    except Exception as e:
        logging.error(f"Error saving deposit: {e}")
        print(f"Error saving deposit: {e}")

# function to get details of a transaction
def get_transaction_details(tx_hash):
    try:
        transaction = w3.eth.get_transaction(tx_hash)
        block = w3.eth.get_block(transaction.blockNumber)
        
        # extract requested data
        deposit_data = {
            'blockNumber': transaction.blockNumber,
            'blockTimestamp': block.timestamp,
            'sender': transaction['from'],  # ensure address is stored as string
            'amount': Web3.from_wei(transaction['value'], 'ether'),
            'hash': transaction['hash'].hex()  # transaction hash as string
        }
        return deposit_data
    except Exception as e:
        logging.error(f"Error fetching transaction {tx_hash}: {e}")
        print(f"Error fetching transaction {tx_hash}: {e}")
        return None

# main function to track deposits
def track_deposits():
    conn, cursor = init_db()  # initialize DB connection
    if not conn or not cursor:
        print("Failed to initialize the database.")
        return
    
    # confirm database file creation
    if os.path.exists('deposits.db'):
        print("Database file 'deposits.db' created successfully.")
    else:
        print("Failed to create the database file.")

    latest_block = w3.eth.get_block('latest').number
    logging.info(f"Tracking deposits from block {latest_block}")
    print(f"Tracking deposits from block {latest_block}")

    while True:
        try:
            # get the latest block
            block = w3.eth.get_block('latest')
            logging.info(f"Checking block {block.number}...")
            print(f"Checking block {block.number}...")

            # iterate over transactions in the block
            for tx_hash in block.transactions:
                tx = w3.eth.get_transaction(tx_hash)

                # log every transaction address for debugging
                logging.info(f"Transaction to address: {tx.to}")
                print(f"Transaction to address: {tx.to}")

                # check if transaction is to the beacon deposit contract
                if tx.to and tx.to.lower() == contract_address:
                    print("reached")
                    deposit_data = get_transaction_details(tx_hash)
                    if deposit_data:
                        save_deposit(deposit_data, cursor, conn)
            time.sleep(300)  # periodically check every 5 minutes
        except Exception as e:
            logging.error(f"Error in tracking deposits: {e}")
            print(f"Error in tracking deposits: {e}")
            time.sleep(300)

if __name__ == "__main__":
    track_deposits()