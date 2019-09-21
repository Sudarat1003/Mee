#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = 10
total = 0.0
#input รับค่าตัวเลขเข้ามาทางแป้นพิมพ์ 10 ครั้ง ด้วยคำสั่ง for
for i in range(n):
    #process เมื่อได้ตัวเลขมาครบทั้ง 10 จำนวนแล้ว นำมาบวกกันแล้วหารด้วยจำนวนตัวทั้งหมดคือ 10
    #Define of variable กำหนดให้ตัวเลชที่รับเข้ามาเป็น float เลขทศนิยม
    number = float(input("Enter number"))
    total = total + number
avg = total/n
#output เมื่อทำขั้นตอน process แล้วได้คำตอบให้แสดง output ออกทางหน้าจอด้วยคำสั่ง print 
print("ค่าเฉลี่ย =", avg)
        


# In[ ]:




