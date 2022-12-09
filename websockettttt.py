from api_helper import ShoonyaApiPy
import credentials
import time
api = ShoonyaApiPy()
k = open("TOKEN",'r')
l = (k.read())
ok = api.set_session(userid=credentials.user, password=credentials.u_pwd, usertoken=l)
token = api.get_quotes('NSE', 'Nifty Bank')['token']
print(token)
api.start_websocket(socket_open_callback=self.__on_open_callback,
                                subscribe_callback=self.__event_handler_quote_update,
                                order_update_callback=self.__event_handler_order_update,
                                socket_error_callback=self.__error_callback,
                                socket_close_callback=self.__socket_closed
                                )


def __on_open_callback(self, ws=None):
    self.open_callback()

def open_callback(self):
    print('app is connected to websocket')
    self.socket_opened = True

def __event_handler_order_update(self, message=None):
    self.event_handler_order_update(message)

def event_handler_order_update(self,message):
    print("order event: " + str(message))