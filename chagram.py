row=int(input("Enter the total rows:"))

'''
a=[]
for i in range(g):
        b=[]
        for j in range(g):
                d=0
                b.append(d)
        a.append(b)
'''

a=[[0 for i in range(row)]for j in range (row)] #iist comprehension method

c=1
i=0;j=0;n=0
while(row>row//2):
        while(j<row):
                a[i][j]=c
                c+=1
                j+=1
        j-=1;i+=1
        while(i<row):
                a[i][j]=c
                c+=1
                i+=1
        i-=1;j-=1
        while(n<=j):
                a[i][j]=c
                c+=1
                j-=1
        j+=1;i-=1
        while(i>n):
                a[i][j]=c
                c+=1
                i-=1
        row-=1;n+=1
        j+=1;i+=1
for i in range(len(a)):
        for j in range(len(a)):
                print("{0:3d} ".format(a[i][j]),end=" ")
        print("\n")

