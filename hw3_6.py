a_list=range(1,11)
a_list=list(range(1,11))
a_list.append(20)
a_list.append(25)

a=a_list[4]
print(a)
b=a_list[-1]
print(b)
c=a_list[0]
print(c)

slice1=a_list[0:5]
print(slice1)
slice2=a_list[:3]
print(slice2)
slice3=a_list[4:]
print(slice3)