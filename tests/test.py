#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("randstr"))

import rs

# Various tests that randstr(string_length, seed_type) method should pass with the 'al' seed_type value. 
def test_al(randstr):
    print("Alpha Lower test start:")

    # Check whether ranstr argument is a string.   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    # Check whether randstr argument is all alphabet letters.   
    assert randstr.isalpha() == True, "The argument randstr isn't all alphabet letters!"
    print("Alpha check complete!")

    # Check whether randstr argument is all lowercase letters.   
    assert randstr.islower() == True, "The argument randstr isn't all lowercase letters!"
    print("Case check complete!")

    # Check whether randstr length is less than 10000.
    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Lower test complete...")

# Various tests that randstr(string_length, seed_type) method should pass with the 'au' seed_type value. 
def test_au(randstr):
    print("Alpha Upper test start:")

    # Check whether ranstr argument is a string.   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    # Check whether randstr argument is all alphabet letters.   
    assert randstr.isalpha() == True, "The argument randstr isn't all alphabet letters!"
    print("Alpha check complete!")

    # Check whether randstr argument is all uppercase letters.   
    assert randstr.isupper() == True, "The argument randstr isn't all uppercase letters!"
    print("Case check complete!")

    # Check whether randstr length is less than 10000.
    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Upper test complete...")

# Various tests that randstr(string_length, seed_type) method should pass with the 'dig' seed_type value. 
def test_dig(randstr):
    print("Digit test start:")

    # Check whether ranstr argument is a string.   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    # Check whether randstr argument is all decimal digits.   
    assert randstr.isdecimal() == True, "The argument randstr isn't all decimal digits!"
    print("Digit check complete!")

    # Check whether randstr length is less than 10000.
    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Digit test complete...")

# Various tests that randstr(string_length, seed_type) method should pass with the 'spec' seed_type value. 
def test_spec(randstr):
    print("Special Digit test start:")

    # Check whether ranstr argument is a string.   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    # Check whether randstr argument is all special characters.   
    assert rs.isspec(randstr) == True, "The argument randstr isn't all special characters!"
    print("Digit check complete!")

    # Check whether randstr length is less than 10000.
    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Special Digit test complete...")

# Various tests that randstr(string_length, seed_type) method should pass with the 'ad' seed_type value. 
def test_ad(randstr):
    print("Alpha Digit test start:")

    # Check whether ranstr argument is a string.   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    # Check whether randstr argument is all alphanumeric characters.   
    assert randstr.isalnum() == True, "The argument randstr isn't all alphanumeric characters!"
    print("Digit check complete!")

    # Check whether randstr length is less than 10000.
    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Digit test complete...")

# Various tests that randstr(string_length, seed_type) method should pass with the 'ads' seed_type value. 
def test_ads(randstr):
    print("Alpha Digit Special test start:")

    # Check whether ranstr argument is a string.   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    # Check whether randstr argument is either upper/lower alphabet, decimal or special characters.   
    assert rs.isads(randstr) == True, "The argument randstr isn't all upper/lower alphabet, decimal or special characters!"
    print("Digit check complete!")

    # Check whether randstr length is less than 10000.
    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Digit Special test complete...")

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
# Run test methods on the strings.  
print("String with random lower case alphabet letters of length", string_length, "\n", "--------------------------------------------------------------") 
print(random_strings[0], "\n")
test_al(random_strings[0])
print()

print("String with random upper case alphabet letters of length", string_length, "\n", "--------------------------------------------------------------") 
print(random_strings[1], "\n")
test_au(random_strings[1])
print()

print("String with random digits 0-9 of length", string_length, "\n", "---------------------------------------")
print(random_strings[2], "\n")
test_dig(random_strings[2])
print()

print("String with random special characters of length", string_length, "\n", "-----------------------------------------------")
print(random_strings[3], "\n")
test_spec(random_strings[3])
print()

print("String with random lower/upper case alphabet letters and digits 0-9 of length", string_length, "\n", "------------------------------------------------------------------------------")
print(random_strings[4], "\n")
test_ad(random_strings[4])
print()

print("String with random lower/upper case alphabet letters, digits 0-9, and special characters of length", string_length, "\n", "---------------------------------------------------------------------------------------------------")
print(random_strings[5], "\n")
test_ads(random_strings[5])

# Delete objects. 
del(string_length, random_strings)