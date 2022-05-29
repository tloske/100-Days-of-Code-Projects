print("Welcome to the tip calculator.")

total = float(input("What was the total bill? ")[1:])
num_people = int(input("How many people to split the bill? "))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))

payment = total/num_people*(1 + tip_percentage/100)

print(f"Each person should pay: ${payment:.2f}")
