from turtle import clear
from brownie import accounts, Restaurant, network, config

LOCAL_ACCOUNT = ["development", "ganache"]


def deploy_contract():
    account = get_account()
    restaurant = Restaurant.deploy({"from": account})
    print(restaurant)
    print(account.balance())
    return restaurant


def get_account():
    if network.show_active() in LOCAL_ACCOUNT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_contract()
