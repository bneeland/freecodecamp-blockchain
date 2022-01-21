from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account

def deploy_fund_me():
    account = get_account()
    # Pass the price feed address to our FundMe contract

    # If we are on a persistent network like Rinkeby, use the associated address,
    # otherwise, deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying mocks")
        mock_aggregator = MockV3Aggregator.deploy(18, 2000_000_000_000_000_000_000, {"from": account})
        price_feed_address = mock_aggregator.address
        print("Mocks deployed")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()
