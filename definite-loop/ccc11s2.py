n = int(input())

line1 = ''
for i in range(n):
    x = input()
    line1+= x

cnt = 0    
for i in range(n):
    x = input()
    if line1[i]==x:
        cnt+=1

print(cnt)