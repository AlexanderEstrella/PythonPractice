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

# if ^ else statements 

#print("Welcome to the rollercoaster!")
#height = int(input("what is your height in cm?"))

#if height >= 120:
 # print("you can ride")
#else:
 # print("sorry you can't ride come again when you are taller")



number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number")
elif number % 2 > 0:
    print("This is an odd number")
  
  
  #leap year 
  
  Year=int(input("Which year do you want to check? "))
firstleap = Year % 4
Secondleap = Year % 100
thirdleap = Year % 400

if firstleap == 0 and Secondleap != 0 or thirdleap == 0:
   print("Leap")
else:
  print("not")


  #Pizza delivery 
  
   print("Welcome to Python Pizza Deliveries!")
Size = input("What is size Pizza do you want? S, M, L ")
add_pepperoni = input("Do want you pepperoni? Y, N ")
extra_cheese = input("Do want you extra cheese? Y, N ")
bill = 0
if Size == "L":
 bill += 25
elif Size == "M":
  bill += 20
else:
 bill += 15
if add_pepperoni == "Y" and Size == "S":
 bill += 2
elif add_pepperoni == "Y" and Size == "M" or Size == "L":
 bill += 3
if extra_cheese == "Y":
 bill += 1

  
print(f"Your final bill is {bill}")

#ride roller coster
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
bill = 0
if height >= 120:
  age = int(input("What is your age?"))
  if age <= 12:
     bill =+ 5
  elif age <= 18:
       bill =+ 7
  elif age > 45 and age < 55:
    bill =+ 0
  else:
    bill =+ 12  
  photos = input("Want photos? Please type Y or N")
  if photos == "Y":
   bill += 3 
  print(f"Final bill is {bill}")
else:
  print("You can't ride")
  
  
  
  
  # love calculator 
  
  name1 = input("What is your name? \n")
name2 = input("What is your name? \n")
newname = name1 + name2

lowercasename = newname.lower() 

t = newname.count("t")
r = newname.count("r")
u = newname.count("u")
e = newname.count("e")
true = t+r+u+e

l = newname.count("l")
o = newname.count("o")
v = newname.count("v")
e = newname.count("e")

love = l+o+v+e

random = str(true) + str(love)

total_score = int(random)

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}."
)
