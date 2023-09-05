num = int(input("Enter a positive number to test: "))
while(num<0):
    num = int(input("Enter a positive number to test: "))
base=2;
number=0;


while(base<num and number==0):
    if(num%base!=0):
        print (base," is NOT a divisor of ",num, ". . . continuing")
    else:
        print (base," is a divisor of ",num, " . . . stopping")
        number=1
    base=base+1
if(number==0):
    print ()
    print (num," is a prime number")
else:
    print()
    print (num," is NOT a prime number!")
