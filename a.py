import numpy as np

n=int(input("Enter Order of Matrix: "))
f=1
while f==1:
    a = np.random.randint(10, size=(n,n))

    sum1=0
    sum2=0
    for i in range(n):
        for j in range(n):
            if i==j:
                sum1+=a[i][j]
            if i+j==n-1:
                sum2+=a[i][j]
    if sum1!=sum2:
        f=1
    else:
        for i in range(n):
            sumr=0
            sumc=0
            for j in range(n):
                sumr+=a[i][j]
                sumc+=a[i][j]
            print(sumr)
            print(sumc)
            if sumr!=sum1 and sumc!=sum1:
                f=1
            else:
                f=0
    if f==0:
        print("Magic")
        print(a)
    else:
        print("N")   