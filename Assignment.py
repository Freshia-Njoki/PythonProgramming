
# Assignment
# Program that checks whether a year is a leap year or not

# Leap year is divisible by four, except for years that are exactly divisible by 100
# but these centurial years are leap years, if they are exactly divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# Program that checks whether an alphabet letter is constant or a vowel
def isVowel(letter):
    vowels = "AEIOUaeiou"
    if letter in vowels:
        return True
    else:
        return False

letter = input("Enter a letter: ")
if isVowel(letter):
    print(letter, "is a vowel.")
else:
    print(letter, "is a consonant.")
