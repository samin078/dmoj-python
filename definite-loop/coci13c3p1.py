
K = int(input())
K+=1

fib = [0]
fib.append(1)

if K>=1:
    for i in range(2, K):
        fib.append(fib[i-1] + fib[i-2])

A=fib[K-2]
B=fib[K-1]
    
print(A, B)