from solcx import compile_standard
import json
from web3 import Web3

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

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
chain_id = 1337
my_address = "0x3Fbd234Af26Ce5eF813De9EC0f3495346d24683F"
private_key = "48736081a5d6f031b25964436619401a437430a9e629ceddfa2b6320d2d3ebaf"

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
print(transaction)
