vowels = 'aeiouy'

while 1:
    str = input()
    if str=='quit!':
        break
    if len(str)>4:
        if str[-3] not in vowels and str[-2:]=='or':
            str = str[:-2] + 'our'
    print(str)