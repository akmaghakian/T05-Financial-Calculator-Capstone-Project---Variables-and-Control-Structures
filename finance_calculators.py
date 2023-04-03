import math
#Firstly we define the options for the user to select
print ("investment - to calculate the amount of interest you'll earn on your investment") 
print ("bond       - to calculate the amount you'll have to pay on a home loan")

print("\n")

#Secondly we use a structure to validate the user selection, to ensure that the right input is given.
while True:
  try:
    user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
    user_selection = user_selection.lower()
    if user_selection == "investment" or user_selection == "bond":
        print("selection entered successfully")
        break;
    else:
        print("Selection should be either investment or bond")   
  except:
    continue

#Thirtdly if the user selects "investment" we apply this code, making it a casefold to ensure that capitals and lowercase are not taken into account.
#And we request the user to input the variables for investment
if user_selection == "investment".lower() :
    deposit_amount = float(input("How much money would you like to deposit?"))
    interest_rate = float(input("What is the percentage interest rate with only numerical characters?"))
    interest_rate_float = float(interest_rate / 100)
    time = float(input("For how many years would you like to invest the deposit amount?"))
    print("\n")
    #Fourthly we ask the user what type of interest is required.
    interest_type = input("Please choose if you want the 'simple' or the 'compound' interest to be calculated:")
    if interest_type == "simple".casefold() :
        A = deposit_amount*(1 + interest_rate_float*time)
        print(A)
    #Fifthly if the user enters compound we apply the compound formula.
    elif interest_type == "compound".casefold() :
            A = deposit_amount * math.pow((1+interest_rate_float),time)
            print (A)
#Sixthly, this is the code applicable for the bond repayment selection.
if user_selection == "bond".casefold() :
     present_value = float(input("What is the present value of the house?"))
     yearly_interest_rate = float(input("What is the yearly interest rate?"))
     yearly_interest_rate_float = float(yearly_interest_rate / 100)
     monthly_interest_rate = float(yearly_interest_rate_float/12)
     number_of_months = float(input("In how many months do you plan to repay the bond?"))
     print("\n")
     repayment = (monthly_interest_rate * present_value)/(1 - (1 + monthly_interest_rate)**(-number_of_months))
     print(repayment)