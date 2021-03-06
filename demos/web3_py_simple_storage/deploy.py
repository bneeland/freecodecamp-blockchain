from solcx import compile_standard
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open('./SimpleStorage.sol', 'r') as file:
    simple_storage_file = file.read()

compiled_sol = compile_standard(
    {
        'language': 'Solidity',
        'sources': {'SimpleStorage.sol': {'content': simple_storage_file}},
        'settings': {
            'outputSelection': {
                '*': {
                    '*': [
                        'abi',
                        'metadata',
                        'evm.bytecode',
                        'evm.sourceMap',
                    ]
                }
            }
        }
    },
    solc_version='0.6.0',
)

with open('compiled_code.json', 'w') as file:
    json.dump(compiled_sol, file)

# Get bytecode
bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

# Get ABI
abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

# Connect to Rinkeby
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/4e412e2e62164cc1b9c3332473f4f595"))
chain_id = 4
my_address = "0x26012CeC5C940e68C1Aea84ba0018c8217F6D943"
private_key = os.getenv("PRIVATE_KEY")

# Create contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the latest transaction count
nonce = w3.eth.getTransactionCount(my_address)
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# Send signed transaction
print("Deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed")

simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Initial value of favourite number
print(simple_storage.functions.retrieve().call())
print("Updating contract...")
greeting_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
signed_greeting_tx = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=private_key
)
tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)
print("Updated")
print(simple_storage.functions.retrieve().call())





# 4:10:00
# https://www.youtube.com/watch?v=M576WGiDBdQ
