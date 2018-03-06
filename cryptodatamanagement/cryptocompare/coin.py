import pandas as pd

SORT_ORDER_KEY = 'SortOrder'
ID_KEY = 'Id'
IMAGE_URL_KEY = 'ImageUrl'
TOTAL_COIN_SUPPLY_KEY = 'TotalCoinSupply'
PRE_MINED_VALUE_KEY = 'PreMinedValue'
ALGORITHM_KEY = 'Algorithm'
SYMBOL_KEY = 'Symbol'
NAME_KEY = 'Name'
FULLY_PREMINED_KEY = 'FullyPremined'
FULL_NAME_KEY = 'FullName'
PROOF_TYPE_KEY = 'ProofType'
SPONSORED_KEY = 'Sponsored'
URL_KEY = 'Url'
COIN_NAME_KEY = 'CoinName'
TOTAL_COINS_FREE_FLOAT_KEY = 'TotalCoinsFreeFloat'
ALL_KEYS = [SORT_ORDER_KEY, ID_KEY, IMAGE_URL_KEY, TOTAL_COIN_SUPPLY_KEY, PRE_MINED_VALUE_KEY, ALGORITHM_KEY, SYMBOL_KEY, NAME_KEY, FULLY_PREMINED_KEY, FULL_NAME_KEY, PROOF_TYPE_KEY, SPONSORED_KEY, URL_KEY, COIN_NAME_KEY, TOTAL_COINS_FREE_FLOAT_KEY]

class Coin:
    
    def __init__(self, coin_dict):
        self.coin_dict = coin_dict
        
    def get_id(self):
        return self.coin_dict[ID_KEY]
    
    def get_symbol(self):
        return self.coin_dict[SYMBOL_KEY]
    
    def get_name(self):
        return self.coin_dict[NAME_KEY]
    
    def get_full_name(self):
        return self.coin_dict[FULL_NAME_KEY]
    
    def get_coin_name(self):
        return self.coin_dict[COIN_NAME_KEY]
    
    def get_total_coin_supply(self):
        return self.coin_dict[TOTAL_COIN_SUPPLY_KEY]
    
    def get_total_coins_free_float(self):
        return self.coin_dict[TOTAL_COINS_FREE_FLOAT_KEY]
    
    def get_url(self):
        return self.coin_dict[URL_KEY]
    
    def get_image_url(self):
        try:
            # sometimes is missing from the coin dict data
            return self.coin_dict[IMAGE_URL_KEY]
        except KeyError:
            return ''
    
    def get_algorithm(self):
        return self.coin_dict[ALGORITHM_KEY]
    
    def get_pre_mined_value(self):
        return self.coin_dict[PRE_MINED_VALUE_KEY]

    def get_fully_premined(self):
        return self.coin_dict[FULLY_PREMINED_KEY]

    def get_proof_type(self):
        return self.coin_dict[PROOF_TYPE_KEY]

    def get_sponsored(self):
        return self.coin_dict[SPONSORED_KEY]
    
    def get_sort_order(self):
        return self.coin_dict[SORT_ORDER_KEY]
    
    def to_dataframe(self):
        return pd.DataFrame([{ 'id': self.get_id(), 'ticker': self.get_symbol(), 'name': self.get_name(),
            'full_name': self.get_full_name(), 'coin_name': self.get_coin_name(), 'total_coin_supply': self.get_total_coin_supply(),
            'total_coins_free_float': self.get_total_coins_free_float(), 'url': self.get_url(), 'image_url': self.get_image_url(),
            'algorithm': self.get_algorithm(), 'pre_mined_value': self.get_pre_mined_value(), 'fully_premined': self.get_fully_premined(),
            'proof_type': self.get_proof_type(), 'sponsored': self.get_sponsored(), 'sort_order': self.get_sort_order() }])
    
    
def main():
    coin = Coin({'SortOrder': '711', 'Id': '25925', 'ImageUrl': '/media/351401/exb.png', 'TotalCoinSupply': '500000000', 'PreMinedValue': 'N/A', 'Algorithm': 'SHA256', 'Symbol': 'EXB', 'Name': 'EXB', 'FullyPremined': '0', 'FullName': 'ExaByte (EXB) (EXB)', 'ProofType': 'PoW', 'Sponsored': False, 'Url': '/coins/exb/overview', 'CoinName': 'ExaByte (EXB)', 'TotalCoinsFreeFloat': 'N/A'})
    print('01 ID ' + str(coin.get_id()))
    print('02 Name', str(coin.get_name()))
    print('03 Full name', str(coin.get_full_name()))
    print('04 Symbol', str(coin.get_symbol()))
    print('05 Coin name', str(coin.get_coin_name()))
    print('06 Total coin supply', str(coin.get_total_coin_supply()))
    print('07 Total coins free float', str(coin.get_total_coins_free_float()))
    print('08 Url', str(coin.get_url()))
    print('09 Image url', str(coin.get_image_url()))
    print('10 Algorithm', str(coin.get_algorithm()))
    print('11 Pre-mined value', str(coin.get_pre_mined_value()))
    print('12 Fully premined', str(coin.get_fully_premined()))
    print('13 Proof type', str(coin.get_proof_type()))
    print('14 Sponsored', str(coin.get_sponsored()))
    print('15 Sort order', str(coin.get_sort_order()))
                                        
    
if __name__ == "__main__":
    main()
