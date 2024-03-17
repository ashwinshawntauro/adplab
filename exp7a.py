sentence=input('Enter a sentence: ')
l_w=sentence.split()
tot_w,tot_u,tot_l,tot_d=0,0,0,0
tot_w=len(l_w)
for i in sentence:
    if i.isdigit():
        tot_d+=1
    elif i.islower():
        tot_l+=1
    elif i.isupper():
        tot_u+=1

print('No of digits: ',tot_d)
print('No of words: ',tot_w)
print('No of upper: ',tot_u)
print('No of lower: ',tot_l)