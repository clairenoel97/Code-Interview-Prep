#cracking the coding interview

#arrays and strings

#1.1: implement an algorithm to determine if a string has all unique characters.
#what if you cannot use additional data structures
def isUnique(user):
  lst = set(user)
  for letter in lst:
      if user.count(letter) > 1:
          print("False")
      else:
          print("True")
#isUnique("Hi, my name is Claire.")

#1.2: Given two strings, write a method to decide if one is a permutation of the other
def checkPermutation(str1, str2):
    if sorted(str1) == sorted(str2):
        print("true")
    else:
        print("false")
#checkPermutation("sflijf", "fslkjf")
#checkPermutation("from", "form")

#1.3: write a method to replace all spaces in a string with '%20'.
#you may assume that the string has sufficient space at the end to hold the additional characters
#and that you are given the length of the string
def URLify(string, length):
    spaceCount = 0
    string = list(string)

    for i in range(length):
        if string[i] == " ":
            spaceCount += 1

    index = length + (spaceCount * 2)
    #print(len(string))
    for i in range(length-1, -1, -1):
        if string[i] != ' ':
            string[index - 1] = string[i]
            index -= 1
        else:
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index = index - 3
    print(''.join(string))
    return string
#URLify("Mr John Smith    ", 13)

#1.4: given a string, write a function to check if it is a permutation of a palindromeself.
#the palindrome does not need to be limited to just dictionary words
from itertools import permutations
def palindromePermutation(string):
    string = string.replace(" ", "").lower()
    palindromeFound = False
    for str in list(permutations(string)):
        if str == str[::-1]:
            print(''.join(str))
            palindromeFound = True
            break
        else:
            palindromeFound = False
    print(palindromeFound)

#palindromePermutation("Tact Coa")
