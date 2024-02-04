a=[[2,3,5],[3,2,6],[3,4,1]]
b=[[2,4,5,1],[3,5,7,3],[5,0,8,5]]
res=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            res[i][j]+=a[i][k]+b[k][j]
print(res)