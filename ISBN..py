#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n1 = int(input("n1 :"))
n2 = int(input("n2 :"))
n3 = int(input("n3 :"))
n4 = int(input("n4 :"))
n5 = int(input("n5 :"))
n6 = int(input("n6 :"))
n7 = int(input("n7 :"))
n8 = int(input("n8 :"))
n9 = int(input("n9 :"))
print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9))
ISBN1to9 = ((10*n1)+(9*n2)+(8*n3)+(7*n4)+(6*n5)+(5*n6)+(4*n7)+(3*n8)+(2*n9))
if (ISBN1to9 + 1) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"1")
elif (ISBN1to9 + 2) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"2")
elif (ISBN1to9 + 3) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"3")
elif (ISBN1to9 + 4) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"4")
elif (ISBN1to9 + 5) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"5")
elif (ISBN1to9 + 6) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"6")
elif (ISBN1to9 + 7) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"7")
elif (ISBN1to9 + 8) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"8")
elif (ISBN1to9 + 9) % 11 == 0:
    print(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+"9")
else:
    print("ERROR")

