#Write a python program to get 3 subject marks out of that find average of two biggest marks
m1=int(input("Enter 1st marks:"))
m2=int(input("Enter 2nd marks:"))
m3=int(input("Enter 3rd marks:"))
if(m1>m2 and m1>m3):
    if(m2>m3):
        print("M1 and M2 are greater")
        print("The average of this number is:",(m1+m2)/2)
    else:
        print("M1 and M3 are greater")
        print("The average of this number is:",(m1+m3)/2)
    
elif(m2>m1 and m2>m3):
    if(m1>m3):
        print("M1 and M2 are greater")
        print("The average of this number is:",(m1+m2)/2)
    else:
        print("M2 and M3 are greater")
        print("The average of this number is:",(m2+m3)/2)
else:        
    if(m1>m2):
        print("M1 and M3 are greater")
        print("The average of this number is:",(m1+m3)/2)
    else:
        print("M2 and M3 are greater")
        print("The average of this number is:",(m2+m3)/2)