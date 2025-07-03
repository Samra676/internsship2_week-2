#Design a command-line survey that:
#Asks the user 5 different questions (e.g., name, favorite food, birth year, favorite number, favorite language)
#Then prints a summary of all responses in sentence format.
#Use formatting to make the output look professional (e.g., f-strings).


name=(input("plz enter your name:"))
food= ( input("plz enter your fav food:"))
birth=(input("plz enter your birth date:"))
fav_num=(input("plz enter your fav number:"))
fav_lang=(input("plz enter your fav language:"))
print(f"your name is {name},and your fav food is {food},your birth date is {birth},your favourite number is {fav_num},and your favourite language is {fav_lang}")
