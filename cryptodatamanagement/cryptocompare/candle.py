import numpy as np
import pandas as pd
import datetime

TIME_KEY = 'time'
CLOSE_KEY = 'close'
HIGH_KEY = 'high'
LOW_KEY = 'low'
OPEN_KEY = 'open'
VOLUMEFROM_KEY = 'volumefrom'
VOLUMETO_KEY = 'volumeto'

class Candle:

    def __init__(self, candle_dict):
        self.candle_dict = candle_dict
        
    def get_time(self):
        return self.candle_dict[TIME_KEY]

    def get_time_string(self):
        return datetime.datetime.fromtimestamp(candle.get_time()).strftime('%Y%m%d.%H%M%S.%f')

    def get_open(self):
        return self.candle_dict[OPEN_KEY]

    def get_high(self):
        return self.candle_dict[HIGH_KEY]

    def get_low(self):
        return self.candle_dict[LOW_KEY]

    def get_close(self):
        return self.candle_dict[CLOSE_KEY]

    def get_volumefrom(self):
        return self.candle_dict[VOLUMEFROM_KEY]

    def get_volumeto(self):
        return self.candle_dict[VOLUMETO_KEY]

    def to_dataframe(self):
        dt = datetime.datetime.fromtimestamp(self.get_time())
        dateString = dt.strftime('%Y%m%d')
        timeString = dt.strftime('%H%M%S.%f')
        interval_range = (self.get_high() - self.get_low()) / self.get_open() if self.get_open() != 0 else np.nan
        return pd.DataFrame([{ 'timestamp': self.get_time(), 'close': self.get_close(), 'high': self.get_high(),
            'low': self.get_low(), 'open': self.get_open(), 'volumefrom': self.get_volumefrom(), 'volumeto': self.get_volumeto(),
            'volume_delta': (self.get_volumeto() - self.get_volumefrom()), 'date': dateString, 'time': timeString,
            'interval_range': interval_range }])

    
def main():
    candle = Candle({"time":1347062400,"close":11.17,"high":11.19,"low":10.77,"open":11,"volumefrom":80575.47,"volumeto":888301.75})
    print('01 time ' + str(candle.get_time()))
    print('02 close ' + str(candle.get_close()))
    print('03 high ' + str(candle.get_high()))
    print('04 low ' + str(candle.get_low()))
    print('05 open ' + str(candle.get_open()))
    print('06 volumefrom ' + str(candle.get_volumefrom()))
    print('07 volumeto ' + str(candle.get_volumeto()))

    
if __name__ == "__main__":
    main()
