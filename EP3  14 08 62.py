#!/usr/bin/env python
# coding: utf-8

# In[21]:


inputRound=int(input("please Enter Number :"))
sum =0
for x in range(inputRound):
     inputNumber = int(input("x :"+str(x+1)+":"))
sum = inputNumber + sum      
print(sum)
     
     
    
    


# In[ ]:


print(list(range(5)))
start = int(input("start:"))
step = int(input("step:"))

for i in range(5):
    print(start+step*i,end=" ")

