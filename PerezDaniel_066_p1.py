# Filename: PerezDaniel_066_p1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME:  Daniel J. Perez Perez
# STUDENT ID:  802-18-9272
# SECTION:  066
############      DEFINE CONSTANTS BELOW      ############
KILOMETERS_PER_MILE = 1.60934
MILE_PER_KILOMETERS = 0.62137119
POUNDS_PER_KILOGRAM = 2.20462262
KILOGRAM_PER_POUNDS = 0.45359237
FAHRENHEIT_PER_CELSIUS = 1.8
CELSIUS_PER_FAHRENHEIT = 32


############       ADD YOUR CODE BELOW        ############

def convert_miles_to_kilometers():
    miles = input('Enter the miles to be converted: ')
    if is_float(miles):
        # Convert string to numeric miles
        miles = float(miles)
        # Conversion should be rounded to 2 decimal places.
        km = round(miles * KILOMETERS_PER_MILE, 2)
        if km >= 0:
            print(miles, 'miles are equivalent to', km, 'kilometers')
        else:
            print(miles, 'is an invalid number')
    else:
        print('Illegal unit of conversion. Input miles are not a number.')

def convert_kilometers_to_miles():
    kilometers = input('Enter the kilometers to be converted: ')
    if is_float(kilometers):
        kilometers = float(kilometers)
        mi = round(kilometers * MILE_PER_KILOMETERS, 2)
        if mi >= 0:
            print(kilometers, 'kilometers are equivalent to', mi, 'miles')
        else:
            print(kilometers, 'is an invalid number')
    else:
        print('Illegal unit of conversion. Input kilometers are not a number.')

def convert_pounds_to_kilograms():
    pounds = input('Enter the pounds to be converted: ')
    if is_float(pounds):
        pounds = float(pounds)
        kg = round(pounds * KILOGRAM_PER_POUNDS, 2)
        if kg >= 0:
            print(pounds, 'pounds are equivalent to', kg, 'kilograms')
        else:
            print(pounds, 'is an invalid number')
    else:
        print('Illegal unit of conversion. Input pounds are not a number.')

def convert_kilograms_to_pounds():
    kilograms = input('Enter the kilograms to be converted: ')
    if is_float(kilograms):
        kilograms = float(kilograms)
        lb = round(kilograms * POUNDS_PER_KILOGRAM, 2)
        if lb >= 0:
            print(kilograms, 'kilograms are equivalent to', lb, 'pounds')
        else:
            print(kilograms, 'is an invalid number')
    else:
        print('Illegal unit of conversion. Input kilograms are not a number.')

def convert_celsius_to_fahrenheit():
    celsius = input('Enter the celsius to be converted: ')
    if is_float(celsius):
        celsius = float(celsius)
        f = round(celsius * FAHRENHEIT_PER_CELSIUS + 32, 2)
        print(celsius, 'celsius are equivalent to', f, 'fahrenheit')
    else:
        print('Illegal unit of conversion. Input celsius are not a number.')

def convert_fahrenheit_to_celsius():
    fahrenheit = input('Enter the fahrenheit to be converted: ')
    if is_float(fahrenheit):
        fahrenheit = float(fahrenheit)
        x = fahrenheit - CELSIUS_PER_FAHRENHEIT
        # this is the division of 5/9
        y = .55555556
        c = round(x * y, 2)
        print(fahrenheit, 'fahrenheit are equivalent to', c, 'celsius')
    else:
        print('Illegal unit of conversion. Input fahrenheit are not a number.')

def convert_miles_per_hour_to_kilometers_per_hour():
    miles_per_hour = input('Enter the miles per hours to be converted: ')
    if is_float(miles_per_hour):
        miles_per_hour = float(miles_per_hour)
        kmph = round(miles_per_hour * KILOMETERS_PER_MILE, 2)
        if kmph >= 0:
            print(miles_per_hour, 'miles per hour are equivalent to', kmph, 'kilometers per hour')
        else:
            print(miles_per_hour, 'is an invalid number')
    else:
        print('Illegal unit of conversion. Input miles per hour are not a number.')

def convert_kilometers_per_hour_to_miles_per_hour():
    kilometers_per_hour = input('Enter the kilometers per hours to be converted: ')
    if is_float(kilometers_per_hour):
        kilometers_per_hour = float(kilometers_per_hour)
        mph = round(kilometers_per_hour * MILE_PER_KILOMETERS, 2)
        if mph >= 0:
            print(kilometers_per_hour, 'kilometers per hour are equivalent to', mph, 'miles per hour')
        else:
            print(kilometers_per_hour, 'is an invalid number')
    else:
        print('Illegal unit cof conversion. Input kilometers per hour are not a number.')

def process_conversion(numericOption):
    if numericOption == 1:
        convert_miles_to_kilometers()
    if numericOption == 2:
        convert_kilometers_to_miles()
    if numericOption == 3:
        convert_pounds_to_kilograms()
    if numericOption == 4:
        convert_kilograms_to_pounds()
    if numericOption == 5:
        convert_celsius_to_fahrenheit()
    if numericOption == 6:
        convert_fahrenheit_to_celsius()
    if numericOption == 7:
        convert_miles_per_hour_to_kilometers_per_hour()
    if numericOption == 8:
        convert_kilometers_per_hour_to_miles_per_hour()
  


    # Add code to handle other menu selections.

############ DO NOT MODIFY THE SECTION BELOW  ############

def is_float(s):
    try:
        float(s)
        # Return True if no exception is thrown
        return True
    except ValueError:
        return False


def print_program_menu():
    print("\n--------")
    print( "Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Miles/hour to kilometers/hour")
    print("8. Kilometers/hour to miles/hour")
    print("9. Exit")


def identify_option(option):
    # Verify that a number was input
    if option.isdigit():
        numericOption = int(option)
        # Check if the selection is within permitted range
        if numericOption >= 1 and numericOption <= 9:
            return numericOption
        else:
            return -1 # Invalid option
    else:
        return -1 # Invalid option


def main():
    done = False
    while not done:
        print_program_menu()
        userOption = input("Enter option: ")
        optionInfo = identify_option(userOption)
        if optionInfo != -1:
            # Option was valid
            if optionInfo == 9:
                done = True
                print ("Thanks for using the unit conversion program!")
            else:
                process_conversion(optionInfo)
        else:
            # Option was invalid
            print ("Invalid option\n")


# This line makes python start the program from the main function
if __name__ == "__main__":
    main()
