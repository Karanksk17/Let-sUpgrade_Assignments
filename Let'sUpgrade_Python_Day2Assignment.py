# Write a Program to calculate the Simple Interest for Bank Customer for Fixed Deposit

# a) If customer is Female & Senior Citizen, Rate - 8%
# b) If customer is Female & Non Senior Citizen, Rate - 6%
# c) If customer is Male & Senior Citizen, Rate - 7%
# d) If customer is Male & Non Senior Citizen, Rate - 5%

# Simple Interest = (Principle Amount * Rate * Time)/100

gender = input("Enter your gender: Press m for Male and f for Female\n")
sc = input("Are you senior citizen: Press y for yes and n for No\n")
principle_amount = int(input("Enter your Principle Amount\n"))
time = int(input("Enter time period in years\n"))

if(gender == 'f' and sc == 'y'):
    print(f"Simple Interest = "+ str((principle_amount *8 * time)/100))
elif(gender == 'f' and sc == 'n'):
    print(f"Simple Interest = "+ str((principle_amount *6 * time)/100))
elif(gender == 'm' and sc == 'y'):
    print(f"Simple Interest = "+ str((principle_amount *7 * time)/100))
elif(gender == 'm' and sc == 'n'):
    print(f"Simple Interest = "+ str((principle_amount *5 * time)/100))
else:
    print("Invalid input")
