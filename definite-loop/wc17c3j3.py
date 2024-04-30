str = input()

n = len(str)
lower = 0
upper = 0
digit = 0

for i in range(n):
    if str[i]>='a' and str[i]<='z':
        lower+=1
    elif str[i]>='A' and str[i]<='Z':
        upper+=1
    elif str[i]>='0' and str[i]<='9':
        digit+=1
        
if (n>=8 and n<=12 and lower>=3 and upper>=2 and digit>=1):
    print('Valid')
else:
    print('Invalid')