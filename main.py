eduMail = input("Enter your edu mail: ")
check = eduMail.endswith("010", 1, 4)
if check:
    print("Valid edu mail for 2010 batch.")
else:
    print("Oops! Invalid edu mail for 2010 batch.\nEdu mail should start by 2010 for this batch.\n")