#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
print("in-out 7:00 - 23:00")
hoursin = int(input("Fill out hours in :"))
timesin = int(input("Fill out time in :"))
hoursout = int(input("Fill out hours out :"))
timesout = int(input("Fill out time out :"))
totalhours1 = hoursout-hoursin
totalhours2 = totalhours1*60
totaltimes1 = timesout-timesin
total = totalhours2+totaltimes1
if total <=15:
    print("0")
elif total <=360:
    totaltime = math.ceil(total/60)
    if totaltime <=3:
        print(totaltime*10)
    else:
        total3 = totaltime-3
        print(30+total3*20)
else:
    print("200")


# In[ ]:




