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

#1.5:there are three types of edits that can be performed on strings:
#insert, delete, and replace. Given 2 strings, write a function to check if they are one edit or zero edits away
def oneAway(str1, str2):
    if str1 == str2:
        print("zero edits away")
    elif len(str1) == len(str2):
        replacement(str1, str2)
    elif len(str1) + 1 == len(str2):
        insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        insert(str2, str1)
    else:
        print("NOOO")

def insert(str1, str2):
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                print("Nore than one edit away")
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    print("One edit away")
    return True

def replacement(str1, str2):
    differenceFound = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if differenceFound:
                print("more than one edit away")
                differenceFound = False
                return
            #print("replaced one letter")
            differenceFound = True
    print("One edit away")
    return differenceFound
# oneAway("pale", "ple")
# oneAway("pales", "pale")
# oneAway("pale", "bale")
# oneAway("pale", "bae")

#1.6: Implement a method to perform basic string compression using the counts of repearted characters
#if the compressed string is smaller than the original string, return the original string
def stringCompression(string):
    output = []
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            count += 1
        else:
            output.append(string[i] + str(count))
            count = 1
    output.append(string[i] + str(count))
    output = ''.join(output)

    if len(output) >= len(string):
        print(string)
    else:
        print(output)
#stringCompression("aabcccaaaababa")

#1.7: Given an image represented by an NxN matrix, where each pixel in the image
#is 4 bytes, write a method to rotate the image by 90 degrees
def rotateMatrix(matrix):
    N = len(matrix)
    printMat(matrix)
    print()
    for x in range(int(N/2)):
        for y in range(x, N-1-x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = temp
    printMat(matrix)

def printMat(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(matrix[row][col], end = " ")
        print("")
#rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

def zeroMatrix(matrix):
    row = [0 for x in range(len(matrix))]
    col = [0 for x in range(len(matrix[0]))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 0:
                row[x] = True
                col[y] = True
    for i in range(len(row)):
        if row[i]:
            nullifyRow(matrix, i)
    for j in range(len(col)):
        if col[j]:
            nullifyCol(matrix, j)

    printMat(matrix)

def nullifyRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
#zeroMatrix([[1,1,1],[0,1,1],[1,1,1]])

#1.8: Assume you ahve a method isSubstring which checks if one word is a substring
#of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
#using one call to isSubstring
def stringRotation(str1, str2):
    length = len(str1)
    if length == len(str2) and length > 0:
        return isSubstring(str1+str1, str2)
    else:
        print("Not the same length")
    return False

def isSubstring(str1, str2):
    if str1.find(str2):
        print("Substring found")
        return True
    else:
        print("Not found")
        return False
stringRotation("waterbottle", "ersbotlewat")
