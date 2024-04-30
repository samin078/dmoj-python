n = int(input())

late = 0
wait = 0

while 1:
    inp = input()
    if inp=='TAKE':
        if n==999:
            n=1
        else:
            n+=1
        late+=1
        wait+=1
    elif inp=='SERVE':
        wait-=1
    elif inp=='CLOSE':
        print(late, wait, n)
        late = 0
        wait = 0
    elif inp=='EOF':
        break