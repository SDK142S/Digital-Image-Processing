import numpy as np
a=np.array([[17,24,18,15,16],
           [23,5,7,14,16],
           [4,6,13,20,22],
           [10,12,19,21,3],
           [11,18,25,2,9]])
print("a")
print(a)
b=int(input("enter the row(0to4):"))
c=int(input("enter the column(0to4):"))
print("element")
print(a[b,c])
N4=[]
if b+1<5:
    N4.append(a[b+1,c])
if b-1>=0:
    N4.append(a[b-1,c])
if c+1<5:
    N4.append(a[b,c+1])
if c-1>=0:
    N4.append(a[b,c-1])
print(N4)

N8=[]
if b+1<5:
    N8.append(a[b+1,c])
if b-1>=0:
    N8.append(a[b-1,c])
if c+1<5:
    N8.append(a[b,c+1])
if c-1>=0:
    N8.append(a[b,c-1])
if b+1<5 and c-1>=0:
    N8.append(a[b+1,c-1])
if b+1<5 and c+1<5:
    N8.append(a[b+1,c+1])
if b-1>=0 and c-1>=0:
    N8.append(a[b-1,c-1])
if b-1>=0 and c+1<5:
    N8.append(a[b-1,c+1])
print(N8)
ND=[]
if b+1<5 and c-1>=0:
    ND.append(a[b+1,c-1])
if b+1<5 and c+1<5:
    ND.append(a[b+1,c+1])
if b-1>=0 and c-1>=0:
    ND.append(a[b-1,c-1])
if b-1>=0 and c+1<5:
    ND.append(a[b-1,c+1])
print(ND)






