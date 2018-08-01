#! /usr/bin/python3.6

# Jorina is a command line assistant
# Version 1.0

import sys

def manual():
    print("\n---- Jorina ----")
    print("Jorina supports weather, football and conversion at the moment.")
    print("Weather for current city: <jorina weather>")
    print("Weather for specific city: <jorina weather 'city name'>")
    print("Football fixture for certain club: <jorina football 'club name'>")
    print("(Fixture is for last game and next game only)")
    print("Conversion supports: lbs to kg, dollar to tk and miles to km")
    print("Conversion usage: <jorina convert 'unit' 'unit'>\n")

def convert(unit_1, unit_2):
    if unit_1 == "lbs" and unit_2 == "kg":
        print("\n---- Jorina ----")
        lbs = int(input("Enter lbs: "))
        kg = lbs * 0.45
        print("Converted: " + str(kg) + " kg\n")
    elif unit_1 == "dollar" and unit_2 == "taka":
        print("\n---- Jorina ----")
        dollar = int(input("Enter dollar: "))
        taka = dollar * 84.80
        print("Converted: " + str(taka) + " taka\n")
    elif unit_1 == "miles" and unit_2 == "km":
        print("\n---- Jorina ----")
        miles = int(input("Enter miles: "))
        km = miles * 1.609
        print("Converted: " + str(km) + " km\n")
    else:
        print("\n---- Jorina ----")
        print("Invalid instructions. ")
        print("For list of usage commands, enter <jorina man>\n")

if len(sys.argv) < 2:
    print("\n---- Jorina ----")
    print("Usage: <jorina 'module'>")
    print("Example: <jorina weather>")
    print("For list of usage commands, enter <jorina man>\n")
elif sys.argv[1] == "man":
    manual()
elif sys.argv[1] == "convert":
    convert(sys.argv[2], sys.argv[3])