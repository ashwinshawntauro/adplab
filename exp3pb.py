def fun():
    l1=[]
    l=[]
    l2=[]
    for i in range(1,10):
        l.append(i)
    for i in range(10,1,-2):
        l1.append(i)
    for i in range(len(l1)):
        l2.append(l[i]+l1[i])
    l2.append(len(l)-len(l1))
    print(l2)
fun()