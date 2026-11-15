age = int(input("enter a number"))
if age >= 80:
    print("ssenior")
elif age >= 60 and age < 80:
    print("senior")
elif age >= 40 and age < 60:
    print("working")
elif age >= 16 and age <40:
    print("teen")
else:
    print("baby")