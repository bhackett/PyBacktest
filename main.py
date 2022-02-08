# https://github.com/ematvey/pybacktest?ref=morioh.com&utm_source=morioh.com
from __future__ import print_function

import pybacktest
import pandas as pd

ohlc = pybacktest.load_from_yahoo('SPY')
# print(ohlc.tail())