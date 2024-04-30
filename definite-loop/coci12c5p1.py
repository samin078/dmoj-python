str = input()

n = len(str)

line = str[0]
for i in range(1, n):
    if str[i]=='|':
        line+=str[i+1]
 
a=0
c=0       
for i in line:
    if i=='C' or i=='F' or i=='G':
        c+=1
    elif i=='A' or i=='D' or i=='E':
        a+=1
        
if a>c:
    print('A-mol')
elif a<c:
    print('C-dur')
else:
    if str[-1]=='A':
        print('A-mol')
    else:
        print('C-dur')