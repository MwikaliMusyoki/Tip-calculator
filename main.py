print("Welcome to the tip calculator")
x = float(input("What is the total bill?"))
y = int(input("How many people to split the bill?"))
t = float(input("What percentage tip would you like to give? 10, 12 or 15?"))
tip = ((t/100*x)+x)/y
print(f"Each person should pay: {tip}")
