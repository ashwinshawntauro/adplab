size=int(input('Enter the number of elements in the list: '))
l=[]
sum=0
prod=1
for i in range(size):
    ele=int(input('Enter the list elements '))
    l.append(ele)
    if(ele%2==0):
        sum=sum+ele
    else:
        prod=prod*ele
print(sum,prod)