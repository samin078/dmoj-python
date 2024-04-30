n = int(input())

v = []
dist = []
neigh = []

for i in range(n):
    v.append(int(input()))
    
v.sort()
i = 1

while i<n:
    dist.append(v[i]-v[i-1])
    dist[i-1]/=2
    i+=1
    
i = 0

while i<n-2:
    neigh.append((dist[i]+dist[i+1]))
    i+=1

neigh.sort()

print(neigh[0])