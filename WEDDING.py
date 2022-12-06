import time
from datetime import timedelta
from api_helper import ShoonyaApiPy
import credentials
import datetime
from datetime import date
import os
import WeddingWaitTime
from pathlib import Path
api = ShoonyaApiPy()
today = date.today()
yesterday = today-timedelta(days=1)
###########################
#########Main Login #############
ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)
ret = ret['susertoken']
f = open('TOKEN','w+')
f.write(ret)
f.close()
########Token Login###########
# k = open("TOKEN",'r')
# l = (k.read())
# ok = api.set_session(userid=credentials.user, password=credentials.u_pwd, usertoken=l)
token = api.get_quotes('NSE', 'Nifty Bank')['token']
lastBusDay = datetime.datetime.today()
# lastBusDay = lastBusDay.replace(hour=WeddingWaitTime.hour, minute=WeddingWaitTime.minutes, second=0, microsecond=0)
lastBusDay = lastBusDay.replace(hour=12, minute=1, second=0, microsecond=0)
k = lastBusDay.timestamp()
ret = api.get_time_price_series(exchange='NSE', token=token, starttime=lastBusDay.timestamp(),endtime=lastBusDay.timestamp(), interval=1)
bnclose = ret[0]['intc']
print("BANKNIFTY-BASE",bnclose)
option_ki_dari_edi = round((int(float(bnclose))), -2)
cehedge_ki_dari_edi = option_ki_dari_edi+1000
pehedge_ki_dari_edi = option_ki_dari_edi-1000
# print(cehedge_ki_dari_edi)
# print(pehedge_ki_dari_edi)
print("BANKNIFTY is at : ",option_ki_dari_edi)
puttoken = f'{"Nifty Bank"} {"PE"} {option_ki_dari_edi}'
calltoken = f'{"Nifty Bank"} {"CE"} {option_ki_dari_edi}'
puthedgetoken = f'{"Nifty Bank"} {"PE"} {pehedge_ki_dari_edi}'
callhedgetoken = f'{"Nifty Bank"} {"CE"} {cehedge_ki_dari_edi}'
put = api.searchscrip(exchange='NFO',searchtext=puttoken)['values'][0]['tsym']
call = api.searchscrip(exchange='NFO',searchtext=calltoken)['values'][0]['tsym']
puthedge = api.searchscrip(exchange='NFO',searchtext=puthedgetoken)['values'][0]['tsym']
callhedge = api.searchscrip(exchange='NFO',searchtext=callhedgetoken)['values'][0]['tsym']
print("ATM PUT :    ",put)
print("ATM CALL :   ",call)
print("CALL HEDGE : ",callhedge)
print("PUT HEDGE :  ",puthedge)
########################################
optionsdatafile = datetime.datetime.today()
optionsdatafile = str(optionsdatafile.date())
print(optionsdatafile)
fileexist = Path(optionsdatafile)
file =open(optionsdatafile,'a+')
file.close()
file = open(optionsdatafile,'r')
fileinformation = file.read()
tpath = f'D:\ALL\cema\{today}'
ypath = f'D:\ALL\cema\{yesterday}'
purathanafile = os.path.exists(ypath)
kothafile = os.path.exists(tpath)
if purathanafile == False:
    print("WEDDING STRATEGY STARTED")
    while True:
        ######################################################
        #Hedges
        CEHEDGE = api.place_order(buy_or_sell='B', product_type='M',
                        exchange='NFO', tradingsymbol=callhedge,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' CE BOUGHT')
        ret = api.get_order_book()
        cebuy = str(float(ret[0]['avgprc']))
        file = open("pricedata.py",'w')
        file.write(f"CE BUY = {cebuy}")
        file.close()
        PEHEDGE = api.place_order(buy_or_sell='B', product_type='M',
                        exchange='NFO', tradingsymbol=puthedge,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' PE BOUGHT')
        ret = api.get_order_book()
        pebuy = str(float(ret[0]['avgprc']))
        file = open("pricedata.py", 'a')
        file.write("\n" f"PE BUY = {pebuy}")
        file.close()
        time.sleep(1)
        ######################################################
        #ATM
        ATMCE = api.place_order(buy_or_sell='S', product_type='M',
                        exchange='NFO', tradingsymbol=call,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' CE SOLD')
        ret = api.get_order_book()
        cesell = str(float(ret[0]['avgprc']))
        file = open("pricedata.py", 'a')
        file.write("\n" f"CE SELL = {cesell}")
        file.close()
        ATMPE = api.place_order(buy_or_sell='S', product_type='M',
                        exchange='NFO', tradingsymbol=put,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' PE SOLD')
        ret = api.get_order_book()
        pesell = float(ret[0]['avgprc'])
        file = open("pricedata.py", 'a')
        file.write("\n" f"PE SELL = {pesell}")
        file.close()
        file = open(optionsdatafile, 'w+')
        file.write("WEDDING-DEPLOYED")
        file.close()
        break
else:
    while True:
        if purathanafile == True:
            print("EXPIRY-DAY MOWAA E ROJU")
            import weddingexpirydaywaittime
            cp_pehedge = int(float(api.get_quotes('NFO',puthedge)['lp']))
            cp_cehedge = int(float(api.get_quotes('NFO',callhedge)['lp']))
            cp_ceatm = int(float(api.get_quotes('NFO',call)['lp']))
            cp_putatm = int(float(api.get_quotes('NFO',put)['lp']))
            # print("CP HEDGE MOWAA",cp_pehedge)
            #################################################################
            import pricedata
            #################################################################
            if cp_pehedge >= pricedata.PE_BUY:
                finalphedge = cp_pehedge - pricedata.PE_BUY
            else:
                finalphedge = pricedata.PE_BUY - cp_pehedge
                ###################################
            if cp_cehedge >= pricedata.CE_BUY:
                finalchedge = cp_cehedge - pricedata.CE_BUY
            else:
                finalchedge = pricedata.CE_BUY-cp_cehedge
                ##################################
            if cp_ceatm >= pricedata.CE_SELL:
                finalce = cp_ceatm - pricedata.CE_SELL
            else:
                finalce = pricedata.CE_SELL-cp_ceatm
                #################################
            if cp_putatm >= pricedata.PE_SELL:
                finalpe = cp_putatm - pricedata.PE_SELL
            else:
                finalpe = pricedata.PE_SELL - cp_putatm
                #################################
            current_profit_or_loss =  ((finalce+finalpe)-(finalchedge-finalphedge))*25
            if current_profit_or_loss >= pricedata.exitprofit:
                #ATM BUY
                ATMCE = api.place_order(buy_or_sell='B', product_type='M',
                                        exchange='NFO', tradingsymbol=call,
                                        quantity=0, discloseqty=0, price_type='MKT',
                                        retention='DAY', remarks=' CE BOUGHT')

                ATMPE = api.place_order(buy_or_sell='B', product_type='M',
                                        exchange='NFO', tradingsymbol=put,
                                        quantity=0, discloseqty=0, price_type='MKT',
                                        retention='DAY', remarks=' PE BOUGHT')
                time.sleep(1)
                #OTM SELL
                CEHEDGE = api.place_order(buy_or_sell='S', product_type='M',
                                          exchange='NFO', tradingsymbol=callhedge,
                                          quantity=0, discloseqty=0, price_type='MKT',
                                          retention='DAY', remarks=' CE BOUGHT')

                PEHEDGE = api.place_order(buy_or_sell='S', product_type='M',
                                          exchange='NFO', tradingsymbol=puthedge,
                                          quantity=0, discloseqty=0, price_type='MKT',
                                          retention='DAY', remarks=' PE BOUGHT')
                exit()
            if current_profit_or_loss <= pricedata.exitloss:
                #ATM BUY
                ATMCE = api.place_order(buy_or_sell='B', product_type='M',
                                        exchange='NFO', tradingsymbol=call,
                                        quantity=0, discloseqty=0, price_type='MKT',
                                        retention='DAY', remarks=' CE BOUGHT')

                ATMPE = api.place_order(buy_or_sell='B', product_type='M',
                                        exchange='NFO', tradingsymbol=put,
                                        quantity=0, discloseqty=0, price_type='MKT',
                                        retention='DAY', remarks=' PE BOUGHT')
                time.sleep(1)
                #OTM SELL
                CEHEDGE = api.place_order(buy_or_sell='S', product_type='M',
                                          exchange='NFO', tradingsymbol=callhedge,
                                          quantity=0, discloseqty=0, price_type='MKT',
                                          retention='DAY', remarks=' CE BOUGHT')

                PEHEDGE = api.place_order(buy_or_sell='S', product_type='M',
                                          exchange='NFO', tradingsymbol=puthedge,
                                          quantity=0, discloseqty=0, price_type='MKT',
                                          retention='DAY', remarks=' PE BOUGHT')
                exit()
            if ((datetime.datetime.now()).time()).hour == 15 and (
            (datetime.datetime.now()).time()).minute >= 15:
                ATMCE = api.place_order(buy_or_sell='B', product_type='M',
                                        exchange='NFO', tradingsymbol=call,
                                        quantity=0, discloseqty=0, price_type='MKT',
                                        retention='DAY', remarks=' CE BOUGHT')

                ATMPE = api.place_order(buy_or_sell='B', product_type='M',
                                        exchange='NFO', tradingsymbol=put,
                                        quantity=0, discloseqty=0, price_type='MKT',
                                        retention='DAY', remarks=' PE BOUGHT')
                time.sleep(1)
                CEHEDGE = api.place_order(buy_or_sell='S', product_type='M',
                                          exchange='NFO', tradingsymbol=callhedge,
                                          quantity=0, discloseqty=0, price_type='MKT',
                                          retention='DAY', remarks=' CE BOUGHT')

                PEHEDGE = api.place_order(buy_or_sell='S', product_type='M',
                                          exchange='NFO', tradingsymbol=puthedge,
                                          quantity=0, discloseqty=0, price_type='MKT',
                                          retention='DAY', remarks=' PE BOUGHT')
                exit()

















