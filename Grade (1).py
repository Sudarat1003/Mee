#!/usr/bin/env python
# coding: utf-8

# In[ ]:


score = float(input("Fill out score :"))
if score >100:
    print("ERROR")
elif score >=80:
    print("A")
elif score >=75:
    print("B+")
elif score >=70:
    print("B")
elif score >=65:
    print("C+")
elif score >=60:
    print("C")
elif score >=55:
    print("D+")
elif score >=50:
    print("D")
elif score <50:
    print("F")
else:
    print("ERROR")

