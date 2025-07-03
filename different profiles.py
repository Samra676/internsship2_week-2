#Create 3 different user profiles (using variables). For each profile, include:
#Name, profession, country, is_employed (Boolean)

#1st profile
name = "sana "
profession="doctor"
country="pakistan"
is_employed=True
#2nd profile 
name2="ali"
profession2="engineer"
country2="pakistan "
is_employed2=False
#3rd profile 
name3="sara"
profession3="developer"
country3="pakistan"
is_employed3= True
print(f"profile1\n  name :{name}\nprofession :{profession}\n country: {country}\n is_employed: {"yes" if is_employed else " no"}\n------------------------------------")
print(f"profile2\n  name :{name2}\nprofession :{profession2}\n country: {country2}\n is_employed: {"yes" if is_employed2 else " no"}\n-------------------------")
print(f"profile3\n  name :{name3}\nprofession :{profession3}\n country: {country3}\n is_employed: {"yes" if is_employed3 else " no"}\n-----------------------------------")