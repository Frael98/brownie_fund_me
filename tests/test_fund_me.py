from scripts.deploy import deploy_fund_me
from scripts.helpful import *
from brownie import network, accounts

import pytest


def test_can_fund_and_withdraw():

    account = get_account()
    fund_me = deploy_fund_me()

    entrance_fee = fund_me.getEntranceFee() + 100
    # Transaction
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    # Verificamos el entrance_fee
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    # Verificamos si podemos retirar
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        pytest.skip("Only for locals networks")

    # Verificando retiro de no propietario
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    fund_me.withdraw({"from": bad_actor})
