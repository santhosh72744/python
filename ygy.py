# -1 42 65 1 -4 and 6 write a program to find the second smallest negative number from the list
l=[22,-1,42,65,1,-4,6]
m1=999
m2=999
for i in range(len(l)):
    if l[i]<m1:
       m2=m1
       m1=l[i]
print(m2)
