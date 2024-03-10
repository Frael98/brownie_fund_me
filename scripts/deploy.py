from scripts.helpful import *
from brownie import FundMe, config, network, MockV3Aggregator


def deploy_fund_me():
    
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        print(f"The active network is {network.show_active()}")
        MockV3Aggregator.deploy(8, 200000000000, {"from": get_account()})
        price_feed_address = MockV3Aggregator[-1].address # Escoge el ultimo desplegado
        print("Mock desplegado")
    
    account = get_account()
    contract = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )  # Parametro publish_source -> verificar el contrato
    print(f"Desplegado contrato {contract.address}")
    
    return contract


def main():
    deploy_fund_me()
