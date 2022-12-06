CE_BUY = 1
PE_BUY = 1
CE_SELL = 1
PE_SELL = 1
maxprofit = ((PE_BUY+CE_BUY)-(PE_SELL+CE_SELL))*25
exitprofit = round(int(float(maxprofit/3)),-2)
exitloss = -exitprofit
maxloss = ((PE_BUY+CE_BUY)+(PE_SELL+CE_SELL))*25
print(round(int(float(maxprofit)),-2))
print(maxprofit)
print(exitprofit)
print(exitloss)
###################################
# cp_pehedge = 100
# cp_cehedge = 100
# cp_ceatm = 200
# cp_putatm = 200
# puthedge = 500
# maxprofit = 10000
# exitprofit = 9000
# exitloss = -5000