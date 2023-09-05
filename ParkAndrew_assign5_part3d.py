"""
Assignment #5, Part 3
Andrew Park
"""

Start=int(input("Start number: "))
End=int(input("End number: "))

p1=0
p2=0
p3=1

for n in range(Start,End):
    p2=0

#prime or not
    for i in range(2,n):
        if(n%i==0):
            p2=1
            break

#if prime and spacing (spacing of 5)
    if(p2==0 and n!=1):
        print("{:5d}".format(n)," ",end="")
        p1+=1
        p3=p1

#only 10 numbers are printed
    if(p1%10==0 and p3==p1):
        print("")
        p3+=1
