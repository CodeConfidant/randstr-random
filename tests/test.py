#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("randstr"))

import rs

# Prompt user for an int representing the length of the example strings. Max value is 10000.  
def lengthinput():
    string_length = input("Enter the desired length (Max 10000): ")

    if(string_length.isdecimal() == False):
        print("The designated length of the strings must include only decimal values!")
        return lengthinput()
    elif(int(string_length) <= 0):
        print("The designated length of the strings cannot be less than or equal to 0!")
        return lengthinput()
    elif(int(string_length) > 10000):
        print("The designated length of the strings cannot be greater than 10000!")
        return lengthinput()
    else:
        return int(string_length)

# Get desired string length. Max 10000 for this demo. 
string_length = lengthinput()
print()

# Generate the random strings in a list based on that length. 
random_strings = list([
    rs.randstr(string_length, "al"),
    rs.randstr(string_length, "au"),
    rs.randstr(string_length, "dig"),
    rs.randstr(string_length, "spec"),
    rs.randstr(string_length, "ad"),
    rs.randstr(string_length, "ads")
])

# Output the random string combinations of the desired length to terminal. 
print("String with random lower case alphabet letters of length", string_length, "\n", "--------------------------------------------------------------") 
print(random_strings[0], "\n")

print("String with random upper case alphabet letters of length", string_length, "\n", "--------------------------------------------------------------") 
print(random_strings[1], "\n")

print("String with random digits 0-9 of length", string_length, "\n", "---------------------------------------")
print(random_strings[2], "\n")

print("String with random special characters of length", string_length, "\n", "-----------------------------------------------")
print(random_strings[3], "\n")

print("String with random lower/upper case alphabet letters and digits 0-9 of length", string_length, "\n", "------------------------------------------------------------------------------")
print(random_strings[4], "\n")

print("String with random lower/upper case alphabet letters, digits 0-9, and special characters of length", string_length, "\n", "---------------------------------------------------------------------------------------------------")
print(random_strings[5], "\n")

# Delete objects. 
del(string_length, random_strings)