import pandas as pd
import numpy as np
import requests
import os

from dotenv import load_dotenv
load_dotenv()

#env variables
FINNHUB_API_KEY = os.getenv('FINNHUB_API_KEY')
IEX_API_KEY = os.getenv('IEX_API_KEY')


STOCK = 'ag'

IEX = f'https://YOUR_WORKSPACE.iex.cloud/v1/data/core/quote/{STOCK}?token={IEX_API_KEY}'


resp = requests.get(IEX)

print(resp)

resp = resp.json()

print(resp)
