#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator!")

bill = input("What is the Total Bill : $")
tip = input("How much tip would you like to give : ")
people = input("How many people to split the bill : ")

bill_as_float=float(bill)
tip_as_int=int(tip)
people_as_int=int(people)

payment = (bill_as_float + (bill_as_float * (tip_as_int / 100))) / people_as_int
final_payment = round(payment,2)


print(f"Each person should pay : ${final_payment}")



