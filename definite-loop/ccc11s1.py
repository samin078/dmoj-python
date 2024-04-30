n = int(input())

t = 0
s = 0

for i in range(n):
    line = input()
    for j in line:
        if j=='t' or j=='T':
            t+=1
        elif j=='s' or j=='S':
            s+=1
        
if t<=s:
    print('French')
else:
    print('English')