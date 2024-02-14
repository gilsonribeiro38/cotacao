import requests
from datetime import datetime


req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

req_dic = req.json()
cot_dollar = req_dic["USDBRL"]["bid"]
cot_euro = req_dic["EURBRL"]["bid"]
cot_btc = req_dic["BTCBRL"]["bid"]

print(f"Cotação Atualizada. {datetime.now()}\nDólar: R${cot_dollar}\nEuro: R${cot_euro}\nBTC: R${cot_btc}")