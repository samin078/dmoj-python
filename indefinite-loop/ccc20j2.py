p = int(input())
n = int(input())
r = int(input())

new = n
ppl = n
day = 0


while ppl<p:
    day+=1
    new = r*new
    ppl+= new
    
if ppl==p:
    print(day+1)
else:
    print(day)