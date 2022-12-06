from api_helper import ShoonyaApiPy
import credentials
api = ShoonyaApiPy()
k = open("TOKEN",'r')
l = (k.read())
ret = api.set_session(userid=credentials.user, password=credentials.u_pwd, usertoken=l)
print(ret)
api.place_order(buy_or_sell='S', product_type='I',
                exchange='NFO', tradingsymbol='BANKNIFTY08DEC22C48000',
                quantity=25, discloseqty=0, price_type='MKT',
                retention='DAY', remarks=' CE BOUGHT')
ret = api.get_order_book()
cebuy = ret[0]['avgprc']
print(cebuy)
