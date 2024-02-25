sentence=input('Enter the sentence: ')
tot_w,tot_d,tot_u,tot_l=0,0,0,0
tot_w=len(sentence.split())
for i in sentence:
    if i.isdigit():
        tot_d+=1
    elif i.isupper():
        tot_u+=1
    elif i.islower():
        tot_l+=1
    
print('No of words: ',tot_w)
print('No of digits: ',tot_d)
print('No of lowercase: ',tot_l)
print('No of uppercase: ',tot_u)