l1=[2,3,5,3,5,2,4]

for ele in range(len(l1)):
    if(l1[ele]%5==0) and (l1[ele]%3==0):
        l1[ele]='pppqqq'
    elif(l1[ele]%5==0):
        l1[ele]='ppp'
    elif(l1[ele]%3==0):
        l1[ele]='qqq'
    
print(l1)
