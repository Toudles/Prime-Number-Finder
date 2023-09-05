"""
Assignment #5, Part 3
Andrew Park
"""

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

start = int(input("Start number: "))
end = int(input("End number: "))

while (start > end):
    print("End number must be greater than start number")
    start = int(input("Start number: "))
    end = int(input("End number: "))
    
while (start < 0 or end < 0):
    print("Start and end must be postiive")
    start = int(input("Start number: "))
    end = int(input("End number: "))
    
a = start
while (a <= end):
    b = prime(a)
    if (b==0):
        print(a)
    a = a+1





