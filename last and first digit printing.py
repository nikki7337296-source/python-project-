n = int(input('enter a number:'))
ld = n%10
while n>0:
    fd = n%10
    n = n//10
print('first digit:',fd)
print('last digit:' ,ld)