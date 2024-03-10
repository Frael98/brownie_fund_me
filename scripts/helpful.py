from brownie import config, accounts, network

LOCAL_BLOCKCHAIN_ENVIROMENTS = ['development', 'ganache-local']
FORKED_BLOCKCHAIN_ENVIROMENTS = ['mainnet-fork', 'mainnet-fork-dev']

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or network.show_active() in FORKED_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])