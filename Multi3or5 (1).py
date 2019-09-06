#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = int(input("enter number :"))
sum = 0
for number in range(1, number):
    if number % 3 == 0 or number % 5 == 0:
        sum = sum + number
print(sum)

