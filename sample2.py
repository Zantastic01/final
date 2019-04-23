import os
import random
import pygame

# Window
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "CONVERTER 900"

kilometer = {"inch":39370.1, "feet":3280.84, "yard":1093.61, "mile":0.621371, "centimeter":100000, "meter":1000, "micrometer":11.7182818285, "millimeter":1000000, "nanometer":14.7182818285, "kilometer":1}
centimeter = {"inch": 0.393701, "feet":0.0328084, "yard":0.0109361, "mile":10.8905877975, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer":-2.28171817154}
feet = {"inch": 12, "feet":1, "yard":0.333333, "mile":0.000189394, "centimeter":30.48, "meter":0.3048, "micrometer":304800, "millimeter":304.8, "nanometer":16.2853230131, "kilometer":0.0003048}
inch = {"inch": 1, "feet":0.0328084, "yard":0.0109361, "mile":0.621371, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer": 1.90443584429}
centimeter = {"inch": 0.393701, "feet":0.0328084, "yard":0.0109361, "mile":10.8906149803, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer":21.1827661208}
centimeter = {"inch": 0.393701, "feet":0.0328084, "yard":0.0109361, "mile":10.8906149803, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer":21.1827661208}
centimeter = {"inch": 0.393701, "feet":0.0328084, "yard":0.0109361, "mile":10.8906149803, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer":21.1827661208}
centimeter = {"inch": 0.393701, "feet":0.0328084, "yard":0.0109361, "mile":10.8906149803, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer":21.1827661208}
centimeter = {"inch": 0.393701, "feet":0.0328084, "yard":0.0109361, "mile":10.8906149803, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer":21.1827661208}
centimeter = {"inch": 0.393701, "feet":0.0328084, "yard":0.0109361, "mile":10.8906149803, "centimeter":1, "meter":0.01, "micrometer":10000, "millimeter":10, "nanometer":9.71828182846, "kilometer":21.1827661208}



def title():
    print("CONVERTER 900")
    print()
    

def units():
    choice1 = input("""
                        1. centimeter
                        2. feet
                        3. inch
                        4. kilometer
                        5. meter
                        6. micrometer
                        7. millimeter
                        8. nanometer
                        9. yard
                        10. mile
                   Which unit would like you like to start with:   """)
    choice1 = str(choice1)

  
    choice2 = input("""
                        1. centimeter
                        2. feet
                        3. inch
                        4. kilometer
                        5. meter
                        6. micrometer
                        7. millimeter
                        8. nanometer
                        9. yard
                        10. mile
                   Which unit would like you like to start with:   """)

    return convert(choice1, choice2)






def convert(choice1, choice2):
    amount = float(input("enter " + choice1 + " here: "))

    if choice1 == "kilometer":
             conversion = amount * kilometer[choice2]
             
    if amount > 1:
        print(str(amount) + " " + str(choice1) + "s" + " is equal to " + str(conversion) + " " + str(choice2) + "s" + ".")
    else:
        print(str(amount) + " " + str(choice1) + " is equal to " + str(conversion) + " " + str(choice2) + "s" + ".")

def convert_again():
    decision = input("Would you like to convert another unit? (y/n)")
    if decision == 'y' or decision == 'yes':
        return units()
    elif decision == 'n' or decision == 'no':
        return end()
    else:
        print("I don't understand. Please enter 'y' or 'n'.")
        
    
def end():
    print("Thank you for using the CONVERTER 9000")

    
title()
units()
convert_again()

