from brownie import network, config, accounts

def get_account():
    if network.show_active() == "developments":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
