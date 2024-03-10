from scripts.helpful import *
from brownie import FundMe


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print("Funding ...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
