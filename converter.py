print("Converter between miles and kilometres")

while True:
    amount = float(input("Enter the amount: "))
    converted_unit = input("Enter the unit do you want to convert to(m/km): ").casefold()

    miles = amount*0.621371
    kilometres = amount*1.60934

    if converted_unit == "m" or converted_unit == "miles":
        print(f"{amount} kilometers is {miles:.2f} miles")
    elif converted_unit == "km" or converted_unit == "kilometers" or converted_unit == "kilometres":
        print(f"{amount} miles is {kilometres:.2f} kilometres")

    reload = input("Would you like to do another conversion? y/n:" ).casefold()

    if reload == "n": #this will reload the converter for anything except n
        break