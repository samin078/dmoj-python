playlist ='ABCDE'

while 1:
    b = int(input())
    n = int(input()) 
    if b==1:
        for i in range(n):
            playlist = playlist[1:] + playlist[0]
    elif b==2:
        for i in range(n):
            playlist = playlist[-1] + playlist[0:4]
    elif b==3:
        for i in range(n):
            playlist = playlist[1] + playlist[0] + playlist[2:5]
    elif b==4:
        if n==1:
            break
    
print(" ".join(playlist))