A=int(input())
f1=0
f2=1
for i in range(A+1):
    print(f1,end=" ")
    f3=f1+f2
    f1=f2
    f2=f3
