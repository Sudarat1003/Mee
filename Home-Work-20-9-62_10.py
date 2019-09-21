#!/usr/bin/env python
# coding: utf-8

# In[12]:


#input รับค่าตัวเลขเข้ามาทางแป้นพิมพ์
#Define of variabie กำหนดให้ตัวเลขที่รับเข้ามาทางแป้นพิมพ์เป็น int หรือจำนวนเต็ม
number = int(input("Enter number :"))
#process คำเงื่อนไข for โดยจะแสดงแม่สูตรคูณถึง x 12 ของตัวเลขที่รับเข้ามาทางแป้นพิมพ์
for i in range(1,13):
    #output เมื่อทำขั้นตอน process แล้วได้คำตอบ output ให้แสดงผลออกทางหน้าจอด้วยคำสั่ง print
    print(number,"x",i,"=",number*i)
    


# In[ ]:




