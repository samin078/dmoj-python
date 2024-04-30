str = input()
vowel = 'aeiou'

res = ''
i=0
while i<len(str):
    res+=str[i]
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':       
        i+=3
    else:
        i+=1
        
print(res)