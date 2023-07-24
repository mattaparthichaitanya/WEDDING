import credentials
from api_helper import ShoonyaApiPy
api = ShoonyaApiPy()
ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)
ret = ret['susertoken']
f = open('TOKEN','w+')
f.write(ret)
f.close()
print("TOKEN GENERATED")

