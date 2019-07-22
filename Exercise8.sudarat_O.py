#!/usr/bin/env python
# coding: utf-8

# In[1]:


#นางสาว สุดารัตน์ อ่อนดี 362515241017 EE36241N
s=input("Username :")
o=input("Password :")
if s=="mee" and o=="1003":
    print("Welcome to mini Shop.")
else :
    print("Error ,please try again.")
s=30
o=10
m=25
e=20
b=40
print("-------------------Menu-------------------")
print("Welcome to mini Shop")
print("1.limes   30 THB")
print("2. kiwi    80 THB")
print("3. celery 45 THB")
print("4. kale       50 THB")
print("5. avocado 50 THB")
Sidarat=int(input("What do you want?(1-5) : "))
num=int(input("How many do you want? : "))
if Sidarat==1:
    print("You order ",num," of limes ",s*num, " THB")
elif Sidarat==2:
    print("You order ",num," of  kiwi ",o*num, " THB")
elif Sidarat==3:
    print("You order ",num," of celery  ",m*num, " THB")
elif Sidarat==4:
    print("You order ",num," of kale ",e*num, " THB")
elif Sidarat==5:
    print("You order ",num," of avocado",b*num, " THB")


# In[ ]:




