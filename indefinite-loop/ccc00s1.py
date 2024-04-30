n = int(input())

a = int(input())
b = int(input())
c = int(input())

machine = 0
cnt=0

while n>0:
    if machine==0:
        if a!=34:
            a+=1
        else:
            n+=30
            a=0
        machine=1
    elif machine==1:
        if b!=99:
            b+=1
        else:
            n+=60
            b=0
        machine=2
    elif machine==2:
        if c!=9:
            c+=1
        else:
            n+=9
            c=0
        machine=0
    n-=1
    cnt+=1
    
print('Martha plays', cnt,'times before going broke.')