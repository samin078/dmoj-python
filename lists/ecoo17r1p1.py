
for x in range(10):

    cost = int(input())
    year = input()
    n = int(input())

    year = year.split()

    price = [12, 10, 7, 5]
    stud = []
    for i in range(4):
        year[i] = float(year[i])
        stud.append(int(year[i]*n))
    
    total = sum(stud)
    if total!=n:
        idx = stud.index(max(stud))
        stud[idx] += n - total 
    
    for i in range(4):
        price[i] = stud[i]*price[i]
    
    total = sum(price)
        
    if total/2<cost:
        print('YES')
    else:
        print('NO')
