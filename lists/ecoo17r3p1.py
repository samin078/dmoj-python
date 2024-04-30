for data in range(10):
    str = input().split()
    d = int(str[0])
    f = int(str[1])
    
    mat = [[]]
    for i in range(f):
        row = input().split()
        for j in range(d):
            cell = int(row[j])
            mat[i][j] = cell
            
    print(mat)