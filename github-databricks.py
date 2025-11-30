Age=int(input("Enter age: "))
Monthly_income=float(input("Enter monthly income: "))
if Age < 18:
    print ("Not eligible for a bank account.")
elif Age >= 18 and Monthly_income < 15000:
    print ("Eligible for basic savings account.")
elif Age >= 18 and 15000 <= Monthly_income <= 50000:
    print ("Eligible for savings + salary account.")
elif Age >= 18 and Monthly_income > 50000:
    print ("Eligible for premium account.")