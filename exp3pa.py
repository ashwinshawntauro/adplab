def check(num):
    temp=num
    rev=0
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if(rev==temp):
        print(temp,' is a palindrome')
    else:
        print(temp,' is not a palindrome')

num=int(input('Enter a number'))
check(num)