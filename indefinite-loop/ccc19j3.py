n = int(input())

for i in range(n):
    cnt = 1
    i=1
    inp = input()
    num = ''
    while i<len(inp):
        if inp[i]!=inp[i-1]:
            num+= str(cnt) + ' ' + inp[i-1] + ' ' 
            cnt=1
        else:
            cnt+=1
        i+=1
    num+= str(cnt) + ' ' + inp[-1]
    print(num)