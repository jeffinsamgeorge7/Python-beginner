number=35
x=int(input("Enter the number (between 1-50): "))
if number==x:
    print("Your guessing is right")
elif x>=1 and x<=20:
    print("Your guessing is too low")
elif x>=20 and x<=30:
    print("Your guessing is low")
elif x>=30 and x<=40:
    print("your guessing is near")
elif x>=40 and x<=50:
    print("Your guessing is high")
else:
    print("You should use number below 50")
    
