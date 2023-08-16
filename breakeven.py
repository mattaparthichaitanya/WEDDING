import pricedata
import strike
cesell = pricedata.CESELL
pesell = pricedata.PESELL
cebuy  = pricedata.CEBUY
pebuy = pricedata.PEBUY
netdata = round(cesell+pesell-cebuy-pebuy)
print(netdata)
cestrike = strike.CALL
print(cestrike)
mainstrike = int(cestrike[-5:])
print(mainstrike)
upperbreakeven = mainstrike+netdata
lowerbrekeven = mainstrike-netdata
print("UPPER BE",upperbreakeven)
print("LOWER BE",lowerbrekeven)
