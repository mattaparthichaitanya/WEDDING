import credentials
from api_helper import ShoonyaApiPy
api = ShoonyaApiPy()
k = open("TOKEN",'r')
l = (k.read())
ok = api.set_session(userid=credentials.user, password=credentials.u_pwd, usertoken=l)
ret = api.get_positions()[0]['rpnl']
print(ret)