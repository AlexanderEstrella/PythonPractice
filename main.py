print("Welcome to the Rapper Name Generator")
City = input("What's the name of the city you grew up in?\n")
pet = input("what is the name of your favorite pet?\n")
print("Your Rapper name could be " + City + " " + pet)


# ----------------------------------------
# Data types

two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
newdigit = int(two_digit_number[0])
newdigits = int(two_digit_number[1])
print(newdigit + newdigits)

# string
# integer
# float
# boolean


# ----------------------------------

# BMI cal

height = float(input("What is your height? "))
weight = int(input("What is your weight (kg)? "))
Bmi = weight / (height**2)
print(int(Bmi))

#----------------------------------

# LifeinWeeks cal
CurrentAge = int(input("What is your current age? "))
MaximumAge = 90
Numberofexpectedyears = (MaximumAge - CurrentAge)
NumberOfDays = Numberofexpectedyears * 365
NumberOfWeeks = Numberofexpectedyears * 52
NumberofMonths = Numberofexpectedyears * 12
print(f"You have {NumberOfDays} days, {NumberOfWeeks} weeks, and {NumberofMonths} left")



# tip calculator 
Whatisthetotalbill = float(input("What is your total bill? "))
AmountOfTip = int(input("What amount would you like to tip? 10? 12? 15? "))
HowmanyPeople = int(input("How many people dined with you? "))
Percentage = AmountOfTip / 100
Newtotalbillaftertip = Whatisthetotalbill * Percentage
EachPersonWillPay = (Whatisthetotalbill +  Newtotalbillaftertip) / (HowmanyPeople + 1)
final_amount =  round(EachPersonWillPay,2)
final_amount = "{:.2f}".format(EachPersonWillPay)
print(f"Each person will pay: ${final_amount}")
