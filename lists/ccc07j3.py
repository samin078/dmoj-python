n = int(input())

amount = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
total = sum(amount)
elm = 0

for i in range(n):
    elm+=amount[int(input())-1]

banker = int(input())  
remain = (total-elm)/(10-n)

if banker>remain:
    print('deal')
else:
    print('no deal')
