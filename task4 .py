#Create a data type tester:
#Ask the user to input any value., Detect and print what Python guesses its type as (use type()).
#Add conditions to identify if it's likely an integer, float, or string, and print a message like:

x=input("plz enter any value it will tell you the type of input:")
if x .isdigit():
  print("the input is interger. ")
elif "." in x:
    try:
        float(x)
        print("the input is float.")
    except ValueError:
     print ("input num is string ")
    