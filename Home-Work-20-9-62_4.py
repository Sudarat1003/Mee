#!/usr/bin/env python
# coding: utf-8

# In[16]:


#input รับค่าตัวเลขสามจำนวนเข้ามาทางแป้นพิมพ์
#Define of variable กำหนดค่าให้ตัวแปลทั้งหมดเป็น int หรือจำนวนเต็ม
n1,n2,n3 = (int(e) for e in input("number :").split())
#process นำตัวเลขสามจำนวนมาเข้าคำสั่ง if เพื่อหาจำนวนที่มากที่สุดหรือเท่ากัน
if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
elif n3>n1 and n3>n2:
    print(n3)
else:
    print("พบตัวเลขมีค่าเท่ากัน")
#output เมื่อทำขั้น process แล้วได้ค่า output ออกมาให้แสดงออกทางหน้าจอด้วยคำสั่ง print


# In[ ]:




