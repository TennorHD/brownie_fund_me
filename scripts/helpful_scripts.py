from eth_account import account
from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 20000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Active Network: {network.show_active()}")
    print("Deploying Mock..")
    # MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    # print("Mocks deployed!")
    if len(MockV3Aggregator) <= 1:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks deployed!")


# def get_address():
#     if network.show_active() == "development":
#         return accounts[0]
#     else:
#         return accounts.add(config["wallets"]["from_key"])
