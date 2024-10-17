n1 = int(input("Enter the frist number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
if(n1>n2 and n1>n3):
    if(n2>n3):
        print("Frist and second are largest:",((n1+n2)/2))
    else:
        print("Frist and third number are largest:",((n1+n3)/2))    
elif(n2>n1 and n2>n3):
    if(n1>n3):
        print("Second and third are largest:",((n3+n2)/2))
    else:
        print("Frist and third number are largest:",((n1+n2)/2))    
elif(n3>n1 and n3>n2):
    if(n1>n2):
        print("frist and third are largest:",((n3+n1)/2))
    else:
        print("Second and third number are largest:",((n1+n2)/2))      
else:
    print("All the number are equal:",n1)