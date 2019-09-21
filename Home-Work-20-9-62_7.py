#!/usr/bin/env python
# coding: utf-8

# In[2]:


max = 0
#input รับตัวเลขจำนวนเต็มเข้ามาทางแป้นพิมพ์
#Define of variable กำหนดให้ค่า max เริ่มต้นที่ 0 และกำหนดให้ตัวเลขที่รับเข้าเป็น int หรือจำนวนเต็ม
number = int(input("Enter number :"))
#process นำตัวเลขที่ได้มา เข้าในเงื่อนไข while ถ้าตัวเลขที่รับเข้ามามีค่ามากกว่า 0 ให้รับเข้ามาเรื่อยๆ แต่ถ้าตัวเลขน้อยกว่า 0 ให้หยุดรับตัวเลข
while number > 0:
    #process แล้วมาเข้าเงื่อนไข if ต่อเพื่อหาตัวเลขที่มีค่ามากที่สุด
    if number > max:
        max = number
    number = int(input("Enter number :"))
#output เมื่อทำขั้นตอน process เสร็จแล้วให้แสดงผล output ออกทางหน้าจอด้วยคำสั่ง print
print("จำนวนที่มีค่ามากที่สุด :", max)


# In[ ]:




