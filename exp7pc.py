odd,even=0,0
for i in range(10,56):
    if i%2==0:
        even+=1
    else:
        odd+=1

print("Number of even numbers ",even)
print("Number of odd numbers ",odd)