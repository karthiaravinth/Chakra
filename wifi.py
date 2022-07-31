import subprocess as sp
a=sp.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split("\n")
a=[i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
for i in a:
        re=sp.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split("\n")
        re=[b.split(":")[1][1:-1] for b in re if "Key Content" in b]
        try:
                print("{:<30}|{:<}".format(i,re[0]))
        except IndexError:
                print("{:<30}|{:<}".format(i," "))


'''

re=sbp.check_output(["netsh","wlan","show","network"])
re=re.decode("ascii")
re=re.replace("\r","")
ls=re.split("\n")
ls=ls[4:]
sid=[]
for x in range(len(ls)):
        if x%5==0:
                sid.append(ls[x])
print(sid)


'''
