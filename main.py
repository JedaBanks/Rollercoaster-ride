print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm"))

bill = 0
if height >= 120:
  print("You can ride the rollercoster!")
  age = int(input("What is your age?"))
  if age < 12:
   bill = 5
   print("Child tickets are $5.")
  elif age <=18:
   bill = 7
   print("Youth tickets are $7.")
  if ((age >= 45) or (age <= 56)):
   print("You can ride the rollercoaster for free.")  
  else:
   bill = 12
   print("Adult tickets are $12.")
    
  
  wantphotos = input("Do you want to take some pictures? Y or N.")
  if wantphotos == "Y":
   bill += 3
   print(f"Your final bill is {bill}.")    
else:
 print("Sorry, you have to grow taller before you can ride.")