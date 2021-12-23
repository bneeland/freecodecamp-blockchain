from brownie import accounts, config

def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

def main():
    deploy_simple_storage()

# https://www.youtube.com/watch?v=M576WGiDBdQ
# 4:39
