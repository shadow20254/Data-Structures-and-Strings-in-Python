#dictonary
a={"alice":95,"bob":50,"krish":98}
b=(input("Enter the student's name:"))
#using if else statement
if b in a:
    print(f"{b}'s marks are: {a[b]}")
else:
    print("Student not found in our dictionary")
