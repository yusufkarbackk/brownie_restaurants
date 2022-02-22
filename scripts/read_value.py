from brownie import Restaurant, accounts
from scripts.deploy import get_account
from web3 import Web3


def read_contract():
    account = get_account()
    print(account.balance())
    print(accounts[2].balance())
    bad_actor = accounts[1]
    print(bad_actor.balance())
    restaurant = Restaurant[-1]
    restaurant.addMenu("baso", Web3.toWei('2', 'Ether'), {"from": account}, )
    restaurant.buyMenu(
        "baso", {"from": bad_actor, "value": Web3.toWei('2', 'Ether')})
    print(restaurant.getOwnerFund())


def main():
    read_contract()
