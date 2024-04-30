n = int(input())

line1 = input()
line2 = input()

count = 0

for i in range(n):
    if line1[i]=='C' and line2[i]=='C':
        count+=1 


print(count)