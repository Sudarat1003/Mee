#!/usr/bin/env python
# coding: utf-8

# In[2]:


sum = 0.0
n = 0
#Define of variable กำหนดให้ sum เท่ากับ 0.0 กำหนดให้ n เท่ากับ 0
number = int(input("Enter number :"))
#input รับค่าตัวเลขเข้ามาทางแป้นพิมพ์
while number > -1:
    #process ทำเงื่อนไข while โดยให้รับตัวเลขเข้ามาเรื่อยๆจนกระทั่งมีการรับตัวเลข -1 เข้ามาจึงหยุดรับตัวเลขแล้วนำตัวเลขทั้งหมดมาบวกกันแล้วหาค่าเฉลี่ย
    sum = sum + number
    n = n + 1
    number = int(input("Enter number :"))
avg = sum / n
#output เมื่อทำขั้นตอน process แล้วได้คำตอบ output ออกมาให้แสดงออกทางหน้าจอด้วยคำสั่ง print
print("Avg =", avg)
    


# In[ ]:




