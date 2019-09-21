#!/usr/bin/env python
# coding: utf-8

# In[3]:


#input รับค่าปี พ.ศ. เข้ามาทางแป้นพิมพ์โดยครั้งแรกรับค่าปี พ.ศ. ในปัจจุบันและครั้งที่สองรับค่าปีที่เกิด
#Define of variable กำหนดให้ค่าที่รับเข้ามาทางแป้นพิมพ์เป็นจำนวนเต็ม int
presentyear = int(input("Enter present year :"))
yearofbirth = int(input("Enter year of birth :"))
#process โดยนำปีปัจจุบันมาลบกับปีที่เกิดเพื่อหาคำตอบ
age = presentyear-yearofbirth
#output คำได้คำตอบจากขั้ย process แล้วก็ output คำตอบออกทางหน้าจอด้วยคำสั่ง print
print("age =" , age)


# In[ ]:




