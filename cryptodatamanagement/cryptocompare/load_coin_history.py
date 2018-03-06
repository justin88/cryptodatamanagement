import urllib.request
import json
import pandas as pd
import numpy as np
from candle import Candle

# Coin history from cryptocompare.com -- 
# { ... , 
#   "Data" : [{ candleDict }],
#   ...
# }
SYMBOL = 'ICX'
REQUEST_URL = 'https://min-api.cryptocompare.com/data/histoday?fsym=' + SYMBOL + '&tsym=USD&limit=3650&aggregate=1&e=CCCAGG'
DATA_KEY = 'Data'

df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close', 'volumefrom', 'volumeto'])
pd.options.display.max_rows = 999
pd.set_option('expand_frame_repr', False)
pd.options.display.max_columns = 999

# load history from api
with urllib.request.urlopen(REQUEST_URL) as response:
    json_object = json.loads(response.read().decode('utf-8'))

    # convert coin history data to dataframe
    count = 0
    for candle_dict in json_object[DATA_KEY]:
        candle = Candle(candle_dict)
        import datetime
        df = df.append(candle.to_dataframe(), ignore_index=True)
        count += 1
        if count % 100 == 0:
            print('Loading candles... ' + str(count))
    
    print(df)
    
    # write to timestamp-named file
    import os
    HISTORY_PATH = '/Users/jschmidt/dev/crypto/cryptodata/cryptocompare/'
    if not os.path.exists(HISTORY_PATH):
        os.mkdir(HISTORY_PATH)
    date_time_file_path = os.path.join(HISTORY_PATH, 'coin_history_daily_' + SYMBOL + '_' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f') + '.csv')
    df.to_csv(date_time_file_path)
    
    # copy to coin_list_recent.csv # TODO symlink instead
    COIN_HISTORY_RECENT_FILE_PATH = os.path.join(HISTORY_PATH, 'coin_history_daily_' + SYMBOL + '_recent.csv')
    df.to_csv(COIN_HISTORY_RECENT_FILE_PATH)

    # number of currencies
    print('Loaded coin history -- daily -- ' + SYMBOL + ' -- (' + date_time_file_path + '), cryptocurrency count: ' + str(len(json_object[DATA_KEY])))
