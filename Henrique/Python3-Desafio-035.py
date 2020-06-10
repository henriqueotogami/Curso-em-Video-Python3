#Challenge 035
#You must to develop a code to read a length of three lines
#And displays to user if them can be or not a triangle.

print("Challenge 035")
a=float(input("Plase, insert the first length:"))
b=float(input("Now, insert the second length:"))
c=float(input("By last, insert the third lenght:"))
#The real condition for the triangle construction is the need of a length of a side be the less than
#sum of the other two sides. And bigger than absolute value of difference between this measures.

if (b+c)>a>((b-c)*-1):
    print("The measures inserteds can to construct a triangle. Letter B")
else:
    if (a+c)>b>((a-c)*-1):
        print("The measures inserteds can to construct a triangle. Letter A")
    else:
        if(a+b)>c>((a-b)*-1):
            print("The measure inserteds can to construct a triangle. Letter C")
        else:
            print("The measures inserteds cannot to construct a triangle.")