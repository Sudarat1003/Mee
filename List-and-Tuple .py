#!/usr/bin/env python
# coding: utf-8

# In[1]:


month_lst = ["Jan", "May", "Jul", "Aug", "Oct", "Dec"]
month_lst.insert(1,"Fed")
month_lst.insert(2,"Mar")
month_lst.insert(3,"Apr")
month_lst.insert(5,"Jun")
month_lst.insert(8,"Sep")
month_lst.insert(10,"Nov")
print("เดือนทั้งหมด =", month_lst)
month_lst.pop(2)
month_lst.pop(5)
month_lst.pop(9)
print("ลบเดือน = ", month_lst)
month_lst1 = month_lst.copy()
print ("เดือนที่เหลืออยู่ =", month_lst1)


# In[2]:


days_lst = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
days_lst.reverse()
print("เรียงจากท้ายไปหน้า =", days_lst)
days_lst.sort()
print("เรียงตามตัวอักษร = ", days_lst)
print ("ตำแหน่ง 3 5 7 คือ", days_lst[5],days_lst[4],days_lst[2])


# In[3]:


brand_cars_tup = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
print("ตำแหน่งของ Benz คือ ", brand_cars_tup.index("Benz"))
print("ตำแหน่งของ Ford คือ ", brand_cars_tup.index("Ford"))
print("ตำแหน่งของ Volvo คือ ", brand_cars_tup.index("Volvo"))
print("รถทั้งหมด คือ",len(brand_cars_tup))
print("มีรถ Suzuki หรือไม่ = ", "Suzuki" in brand_cars_tup)
print("มีรถ Ferrari หรือไม่ = ", "Ferrari" in brand_cars_tup)
print("มีรถ Ford หรือไม่ = ", "Ford" in brand_cars_tup)


# In[ ]:




