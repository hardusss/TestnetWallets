from testnet.interfaces.logs import Logger
from testnet.interfaces import AddressBalanceInterface
from typing import Optional
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

load_dotenv()

class SolAddressBalance(AddressBalanceInterface):
    @staticmethod
    def get_balance(wallet_name: Optional[str] = None, address: Optional[str] = None) -> float:
        try:
            w3 = Web3(HTTPProvider(os.getenv("ETH_RPC_LINK")))
            if w3.is_connected():
                balance = w3.eth.get_balance(address)
            
            else: return 0.0

        except Exception as ex:
            return 0.0
        