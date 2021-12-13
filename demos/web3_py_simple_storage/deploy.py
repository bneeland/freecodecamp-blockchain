from solcx import compile_standard

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
)
print(compiled_sol)
