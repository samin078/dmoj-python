
word = input()
n = len(word)
str = 'HONI'
cnt=0
res=0

for i in range(0,n):
    if word[i]==str[cnt]:
        cnt+=1
        if cnt==4:
            cnt=0
            res+=1
            
print(res)
