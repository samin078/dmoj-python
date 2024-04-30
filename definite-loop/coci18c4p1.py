s = input()
n = int(input())

cnt = 0
uniq = s
for i in range(n):
    x = input()
    if s==x[2]:
        cnt+=1
        s = x[0]
        uniq+=s

print(s)
print(len(set(uniq)))