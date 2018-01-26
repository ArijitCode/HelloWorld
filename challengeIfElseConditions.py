name = input("Welcome! Please enter your name: ")
age =  int(input("Please enter your age {}: ".format(name)))
if 18< age < 31:
    print("Welcome to the Holiday")
elif age < 18 :
    print("please come back in {} years".format(18-age))
else:
    print("sorry sir you are over the age Limit")