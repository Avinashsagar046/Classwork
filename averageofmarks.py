a, b, c = int(input("Enter mark 1:")), int(input("\nEnter mark 2:")), int(input("\nEnter mark 3:"))

if a>b and b>c:
    print("Average of a and b = ", (a+b)/2)
elif a>b and c>b:
    print("Average of a and c = ", (a+c)/2)
elif b>a and c>a:
    print("Average of b and c = ", (b+c)/2)
else:
    print("Average when a=b=c = ", (a+b+c)/3)


