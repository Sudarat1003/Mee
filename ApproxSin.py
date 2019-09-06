#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
x = float(input())
x = math.radians(x%360)
s = f = x
k = 1
while f != 0:
    f *= (-1)*x**2/((2*k)*(2*k+1))
    s += f
    k += 1
print(s)


# In[ ]:




