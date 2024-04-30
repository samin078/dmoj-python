ad = 'ABC'*35
br = 'BABC'*30
go = 'CCAABB'*18

person = { ad:0, br:0, go:0 }

n = int(input())
ans = input()

i=0
while i<n:
    if ad[i]==ans[i]:
        person[0][1]+=1
    if br[i]==ans[i]:
        person[1][1]+=1
    if go[i]==ans[i]:
        person[2][1]+=1
    i+=1

res = max(person[0][1],person[1][1],person[2][1])
print(res)
if res==person[0][1]:
    print('Adrian')
if res==person[1][1]:
    print('Bruno')
if res==person[2][1]:
    print('Goran')

