import pricedata
maxprofit = ((pricedata.PESELL+pricedata.CESELL)-(pricedata.PEBUY+pricedata.CEBUY))*25
exitprofit = round(int(float(maxprofit/3)),-2)
print("profit",exitprofit)
exitloss = -exitprofit
print('loss',exitloss)
# maxloss = ((pricedata.PEBUY+pricedata.CEBUY)+(pricedata.PESELL+pricedata.CESELL))*25
# print(round(int(float(maxprofit)),-2))
# print(maxprofit)
# print(exitprofit)
# print(exitloss)