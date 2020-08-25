#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("../randstr-random"))

import randstr as rs
 
def test_al(randstr):
    print("Alpha Lower test start:")
   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    assert randstr.isalpha() == True, "The argument randstr isn't all alphabet letters!"
    print("Alpha check complete!")
  
    assert randstr.islower() == True, "The argument randstr isn't all lowercase letters!"
    print("Case check complete!")

    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Lower test complete...")
 
def test_au(randstr):
    print("Alpha Upper test start:")
 
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")
   
    assert randstr.isalpha() == True, "The argument randstr isn't all alphabet letters!"
    print("Alpha check complete!")
 
    assert randstr.isupper() == True, "The argument randstr isn't all uppercase letters!"
    print("Case check complete!")

    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Upper test complete...")
 
def test_dig(randstr):
    print("Digit test start:")
   
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")
   
    assert randstr.isdecimal() == True, "The argument randstr isn't all decimal digits!"
    print("Digit check complete!")

    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Digit test complete...")

def test_spec(randstr):
    print("Special Digit test start:")
  
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")
  
    assert rs.isspec(randstr) == True, "The argument randstr isn't all special characters!"
    print("Digit check complete!")

    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Special Digit test complete...")

def test_ad(randstr):
    print("Alpha Digit test start:")
  
    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")

    assert randstr.isalnum() == True, "The argument randstr isn't all alphanumeric characters!"
    print("Digit check complete!")

    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Digit test complete...")

def test_ads(randstr):
    print("Alpha Digit Special test start:")

    assert type(randstr) is str, "The argument randstr isn't a string!"
    print("Type check complete!")
   
    assert rs.isads(randstr) == True, "The argument randstr isn't all upper/lower alphabet, decimal or special characters!"
    print("Digit check complete!")

    assert len(randstr) <= 10000, "The argument randstr length is greater than 10000!"
    print("Length check complete!")

    print("Alpha Digit Special test complete...")
 
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

string_length = lengthinput()
random_strings = list([
    rs.generate(string_length, "al"),
    rs.generate(string_length, "au"),
    rs.generate(string_length, "dig"),
    rs.generate(string_length, "spec"),
    rs.generate(string_length, "ad"),
    rs.generate(string_length, "ads")
])

test_al(random_strings[0])
test_au(random_strings[1])
test_dig(random_strings[2])
test_spec(random_strings[3])
test_ad(random_strings[4])
test_ads(random_strings[5])