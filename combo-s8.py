import itertools

market=["TUI","TUG","TGS","BUI","BUG","OSP","FST","LPE","STF","DAY"]
source=["DIR","STR","AGN","AGC","OTA","VPP","COM","DIT","STA","ECV","HOU","HCC","HCS","STC"]
channel=["PRE","TEL","EMA","FAX","WIN","EVE","WEB","POR","PUB","ALT","RIC","CON"]

for combination in itertools.product(market, source, channel):
    print combination
