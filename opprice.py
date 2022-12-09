from api_helper import ShoonyaApiPy
import credentials
import time
from datetime import datetime
api = ShoonyaApiPy()
k = open("TOKEN",'r')
l = (k.read())
ok = api.set_session(userid=credentials.user, password=credentials.u_pwd, usertoken=l)
token = api.get_quotes('NSE', 'Nifty Bank')['token']
print(token)
info = api.get_security_info(exchange='NSE', token=token)
print(info)
########################################################################
feed_opened = False
feedJson = {}
socket_opened = False
orderJson = {}
def evert_handler_feed_update(message):
    print(message)
    if(('lp'in message)&('tk'in message)):
        feedJson[message['tk']]={'ltp':float(message['lp'])}
def event_handler_order_update(inmessage):
    print(inmessage)
    if(('norenordno' in inmessage) & ('status' in inmessage)):
        orderJson[inmessage['norenordno']]={'status': inmessage['status']}
def open_callback():
    global feed_opened
    feed_opened = True
def setupWebSocket():
    global feed_opened
    api.start_websocket(order_update_callback=event_handler_order_update,subscribe_callback=evert_handler_feed_update,socket_open_callback=open_callback)
    time.sleep(1)
    while(feed_opened == False):
        print("WAITING FOR WEBSOCKET TO OPEN MOWAA")
        pass
    return True
setupWebSocket()
print(api.subscribe([f'NSE|{token}']))
time.sleep(1)
print('\n')
while True :
    ltpmowaa = (feedJson[token]['ltp'])
    print(ltpmowaa)
    
###################################################################################
