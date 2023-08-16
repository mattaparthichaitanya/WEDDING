from datetime import datetime
import time
###########################
shour = 15
smin = 15
squareoffhour = 15
squareoffmin = 35
####################################
hour = abs(shour-5)
if smin < 30:
    minutes = smin+30
    hour = abs(shour-6)
else:
    minutes = abs(smin - 30)
#####################################
sqhour = abs(squareoffhour-5)
if squareoffmin <30:
    sqmin = squareoffmin+30
    sqhour = abs(squareoffhour-6)
else:
    sqmin = abs(squareoffmin-30)
now = datetime.now()
print(minutes)
print(hour)
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
    time.sleep(waittime+10)
    now = datetime.now()
    # print (now.time())
# import main