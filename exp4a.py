size=int(input('Enter the number of elements'))
l=[]
sum=0
prod=1
for i in range(size):
    ele=int(input('Enter an element'))
    l.append(ele)

for num in l:
    if(num%2==0):
        sum=sum+num
    else:
        prod=prod*ele

print(sum)
print(prod)