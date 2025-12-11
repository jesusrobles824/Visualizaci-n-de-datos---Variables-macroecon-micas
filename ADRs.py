import yfinance as yf
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
import re
from matplotlib.dates import date2num
from matplotlib.ticker import FixedLocator
from io import BytesIO
from dateutil.relativedelta import relativedelta
from pandas.tseries.offsets import MonthEnd
import matplotlib.lines as mlines
from datetime import datetime, timedelta
from pandas_datareader import data as web

# Definir la fecha de hoy automáticamente

tickers_adrs = ['BBAR', 'BMA', 'CEPU', 'CRESY', 'EDN', 'GGAL', 'IRS','LOMA',
                'PAM', 'SUPV', 'TEO', 'TGS', 'TS', 'TX', 'YPF']

# Descargar datos históricos de los ADRs y el Merval
adrs = yf.download(tickers_adrs, start='2010-01-01')['Close']
adrs.columns.name = None  # Correcto
adrs.index.name = 'fecha'  # Correcto
adrs = adrs.round(2)

adrs_var = adrs.pct_change() * 100  # en %
adrs_var = adrs_var.round(2)
adrs_var = adrs_var[::-1]
adrs_var.to_csv('ADRs_variacion_porcentual_diaria.csv', index=True)

adrs = adrs[::-1]
adrs.to_csv('ADRs_Precios.csv', index=True)