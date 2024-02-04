num_list=[45,32,54,75,22,10]
print('Original list ',num_list)
for i in range(len(num_list)):
    if(num_list[i]%3==0 and num_list[i]%5==0):
        num_list[i]='pppqqq'
    elif(num_list[i]%5==0):
        num_list[i]='ppp'
    elif(num_list[i]%3==0):
        num_list[i]='qqq'
print(num_list)