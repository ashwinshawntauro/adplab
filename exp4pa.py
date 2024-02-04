size=int(input('Enter the number of items in list '))
l=[]
for i in range(size):
    ele=input('Enter the elements ')
    l.append(ele)
temp=l[0]
for i in range(1,len(l)):
    if(len(l[i])>len(temp)):
        temp=l[i]
print('The longest string ',temp)