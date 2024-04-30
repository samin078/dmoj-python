import math

for i in range(10):

    orange = 0
    blue = 0 
    green = 0
    yellow = 0 
    pink = 0 
    violet = 0 
    brown = 0
    red = 0

    cnt = 0
    while 1:
        inp = input()
        if inp=='orange':
            orange+=1
        elif inp=='blue':
            blue+=1
        elif inp=='green':
            green+=1
        elif inp=='yellow':
            yellow+=1
        elif inp=='pink':
            pink+=1
        elif inp=='violet':
            violet+=1
        elif inp=='brown':
            brown+=1
        elif inp=='red':
            red+=1
        elif inp=='end of box':
            cnt+= ( math.ceil(orange/7) + math.ceil(blue/7) + math.ceil(green/7) + math.ceil(yellow/7)
            + math.ceil(pink/7) + math.ceil(violet/7) + math.ceil(brown/7) ) * 13 + red * 16
            print(cnt)
            break