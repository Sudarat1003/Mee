#!/usr/bin/env python
# coding: utf-8

# In[ ]:


month = int(input("Fill out month :"))
year = int (input("Fill out year :")) 
years = year-543
if month == 1:
    print("31")
elif month ==2:
    if years%4 ==0:
        print("29")
    else:
        print("28")
elif month ==3:
    print("31")
elif month ==4:
    print("30")
elif month ==5:
    print("31")
elif month ==6:
    print("30")
elif month ==7:
    print("31")
elif month ==8:
    print("31")
elif month ==9:
    print("30")
elif month ==10:
    print("31")
elif month ==11:
    print("30")
elif month ==12:
    print("31")
else:
    print("error")

