#Verify if the person can vote and he/she can contest an election

Age = int(input("Enter your Age = "))

if Age >= 25 :
    print("You can Cast your Vote as well as Contest in an Election")
elif Age >= 18 :
    print("You can Cast your Vote")
else:
    print("NOT ELIGIBLE")
