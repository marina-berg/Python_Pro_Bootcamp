print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
finalBill = 0
if size == "S":
    finalBill +=15
    if pepperoni == "Y":
        finalBill +=2
if size == "M":
    finalBill +=20
    if pepperoni == "Y":
        finalBill +=3
if size == "L":
    finalBill +=25
    if pepperoni == "Y":
        finalBill +=3

if extra_cheese == "Y":
    finalBill +=1

print(f"Your final bill is: ${finalBill}.")