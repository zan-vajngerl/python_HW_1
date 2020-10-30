print("Converter between miles and kilometres")

while True:
    amount = float(input("Enter the amount: "))
    converted_unit = input("Enter the unit do you want to convert to(m/km): ").casefold()

    miles = amount*0.621371
    kilometres = amount*1.60934
    miles_list = ["m", "miles", "mile"]
    kilometres_list = ["km", "kilometre", "kilometer", "kilometers", "kilometres", "k"]

    if converted_unit in miles_list:
        print(f"{amount} kilometers is {miles:.2f} miles")
    elif converted_unit in kilometres_list:
        print(f"{amount} miles is {kilometres:.2f} kilometres")

    reload = input("Would you like to do another conversion? y/n:" ).casefold()

    if reload == "n": #this will reload the converter for anything except n
        break