#Write a program that:
#Declares five different variables, Stores a different data type in each (e.g., string, integer, float, boolean, complex)
#Prints their values and data types
#Then, converts each variable to a different type (where possible) and prints the new types
#Note: You may not be able to convert all types - handle errors or comment why.
#data  type 
name ="sana "
age=21
height = 5.4
is_student=True
complex_number=3+ 4j
print ("sana:", type(name))
print ("21:",type(age))
print ("5.4:",type(height))
print ("True :",type(is_student))
print ("3+4j:",type(complex_number))
print ("--------converted data type----------")
#converted data type
name_string =str(name)
age_int=int(age)
height_float=float(height)
is_student_bool=bool(is_student)
complex_number_str=str(complex_number)
print ("name is ",type(name_string))
print("age is ",type(age_int))
print("height is ",type(height_float))
print("is_student is ",type(is_student_bool))
print("complext_number is ",type(complex_number_str))