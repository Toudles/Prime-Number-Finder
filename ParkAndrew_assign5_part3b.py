def prime(num):
    base=2;
    number=0;
    while(base<num and number==0):
        if(num%base!=0):
            number=0
        else:
            number=1
        base=base+1
    return number
a=1
while(a<1000):
    b = prime(a)
    if(b==0):
        if a == 1:
            print("1 is technically not a prime number")
        else:
            print (a," is a prime number!")
    a=a+1

