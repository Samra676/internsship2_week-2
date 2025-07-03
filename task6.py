#Ask the user to:
#Enter their year of birth, Calculate their age (based on current year), Check if the user is eligible to vote (18+ years)

#Display a message:
#"You are eligible to vote." or "You are not eligible to vote yet."


birth_year=(input("please enter your birth year:"))
current_year=(input("please enter the current year:"))
age=int(current_year)-int(birth_year)
print (f"your age is {age} year old ")
if age <18:
    print("you are not  eligible for votes")
else:
    print(" you are eligible for votes")