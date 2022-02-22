from brownie import accounts
from scripts.deploy import deploy_contract, get_account
from web3 import Web3


def test_add_menu():
    account = accounts[0]
    restaurant = deploy_contract()
    restaurant.addMenu("nasi", Web3.toWei(
        '1', 'Ether'), {"from": account})
    allMenu = restaurant.retrieveAllMenu()[0]
    menuCount = restaurant.getMenuCount()
    assert allMenu == "nasi"
    assert menuCount == 1


def test_retrieve_menu():
    account = get_account()

    restaurant = deploy_contract()
    restaurant.addMenu(
        "nasi",  Web3.toWei(
            '1', 'Ether'), {"from": account, })
    menu = restaurant.retrieveMenu("nasi")
    assert menu == ("nasi", 1000000000000000000)


def test_buy_menu():
    account = get_account()
    restaurant = deploy_contract()
    restaurant.addMenu("nasi", Web3.toWei(
        '1', 'Ether'), {"from": account})
    bad_actor = accounts[1]
    tx = restaurant.buyMenu("nasi", {"from": bad_actor, "value": Web3.toWei(
        '1', 'Ether')})
    tx.wait(1)

    assert restaurant.getOwnerFund() == 1000000000000000000
