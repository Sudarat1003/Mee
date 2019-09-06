#!/usr/bin/env python
# coding: utf-8

# In[8]:


mm,dd,yyyy = (str(e) for e in input().split())
if mm == "01" :
    print(dd, "JAN", yyyy)
elif mm == "02" :
    print(dd, "FEB", yyyy)
elif mm == "03" :
    print(dd, "MAR", yyyy)
elif mm == "04" :
    print(dd, "APR", yyyy)
elif mm == "05" :
    print(dd, "MAY", yyyy)
elif mm == "06" :
    print(dd, "JUN", yyyy)
elif mm == "07" :
    print(dd, "JUL", yyyy)
elif mm == "08" :
    print(dd, "AUG", yyyy)
elif mm == "09" :
    print(dd, "SEP", yyyy)
elif mm == "10" :
    print(dd, "OCT", yyyy)
elif mm == "11" :
    print(dd, "NOV", yyyy)
elif mm == "12" :
    print(dd, "DEC", yyyy)
else:
    print("ERROR")


# In[ ]:




