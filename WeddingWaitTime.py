from datetime import datetime
import time
hour = 12
minutes = 00
squareoffhour = 15
squareoffmin = 30
now = datetime.now()
currentTime = now.hour *3600 + now.minute * 60 +now.second + now.microsecond * 0.000001
targetTime = hour*3600 + minutes *60 + 0
print(targetTime)
print(currentTime)
if targetTime < currentTime:
    print("TIME AYIPOYINDI BABOOOIIIIII.............")
    runtime = targetTime

else:
    waittime = targetTime - currentTime
    print("INKA TIME AVVALE MOWAA WAIT SESTUNNNAAA...............")
    # print (waittime)
    time.sleep(waittime+5)
    now = datetime.now()
    # print (now.time())
