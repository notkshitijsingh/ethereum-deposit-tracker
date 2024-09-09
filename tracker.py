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