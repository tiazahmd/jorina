def error():
    print("\n---- Jorina ----")
    print("Usage: <jorina 'module'>")
    print("Example: <jorina weather>")
    print("For list of usage commands, enter <jorina man>\n")

def manual():
    print("\n---- Jorina ----")
    print("Jorina supports weather, football and conversion at the moment.")
    print("Weather for current city: <jorina weather>")
    print("Weather for specific city: <jorina weather 'city name'>")
    print("Football fixture for certain club: <jorina football 'club name'>")
    print("(Fixture is for last game and next game only)")
    print("Conversion supports: lbs to kg, dollar to tk and miles to km")
    print("Conversion usage: <jorina convert 'unit-unit' '0000'>")
    print("Example: <jorina convert lbs-kg 23>\n")

def convert(unit, value):
    if unit == "lbs-kg":
        print("\n---- Jorina ----")
        lbs = int(value)
        kg = lbs * 0.45
        print("Converted: " + str(kg) + " kg\n")
    elif unit == "dollar-taka":
        print("\n---- Jorina ----")
        dollar = int(value)
        taka = dollar * 84.80
        print("Converted: " + str(taka) + " taka\n")
    elif unit == "miles-km":
        print("\n---- Jorina ----")
        miles = int(value)
        km = miles * 1.609
        print("Converted: " + str(km) + " km\n")
    else:
        print("\n---- Jorina ----")
        print("Invalid instructions. ")
        print("For list of usage commands, enter <jorina man>\n")