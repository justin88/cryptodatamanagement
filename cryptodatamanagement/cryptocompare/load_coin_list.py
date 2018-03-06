import urllib.request
import json
import pandas as pd
import numpy as np
from coin import Coin
import datetime

# Coin List from cryptocompare.com -- https://www.cryptocompare.com/api/#-api-data-coinlist-
# { ... , 
#   "Data" : {
#     coinNameString : coinDetailsDict,
#     ...
#   }
# }
REQUEST_URL = 'https://www.cryptocompare.com/api/data/coinlist/'
DATA_KEY = 'Data'

df = pd.DataFrame(columns=['id', 'ticker', 'name'])

# load coin list from api
with urllib.request.urlopen(REQUEST_URL) as response:
    json_object = json.loads(response.read().decode('utf-8'))

    # convert coin list data to dataframe
    count = 0
    for coin_name in json_object[DATA_KEY]:
        coin = Coin(json_object[DATA_KEY][coin_name])
        df = df.append(coin.to_dataframe(), ignore_index=True)
        count += 1
        if count % 100 == 0:
            print('Loading coins... ' + str(count))
        
    # write to timestamp-named file
    import os
    HISTORY_PATH = '/Users/jschmidt/dev/crypto/cryptodata/cryptocompare/'
    if not os.path.exists(HISTORY_PATH):
        os.mkdir(HISTORY_PATH)
    date_time_file_path = os.path.join(HISTORY_PATH, 'coin_list_' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f') + '.csv')
    df.to_csv(date_time_file_path)
    
    # copy to coin_list_recent.csv # TODO symlink instead
    COIN_LIST_RECENT_FILE_PATH = os.path.join(HISTORY_PATH, 'coin_list_recent.csv')
    df.to_csv(COIN_LIST_RECENT_FILE_PATH)

    # number of currencies
    print('Loaded coin list (' + date_time_file_path + '), cryptocurrency count: ' + str(len(json_object[DATA_KEY])))
    