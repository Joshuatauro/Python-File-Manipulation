'''Write a menu driven program to perform / manipulate a text file called as ‘POETIC.TXT’ containing ‘n’ no. of lines , Using the following functions .(The text file is created using the create
function ) also after each function execution the display function must be called to display the contents of the file .
(1) CREATE()

(2) DISPLAY() : to display the complete contents of the file whose name is given by the user .

(3) COUNTCHAR() :read the text file and display the number of vowels/ consonants/ uppercase/ lowercase characters in the file.

(4) HASHSHOW():read the text file “POETIC.TXT “line by line and display each word separated by a #.

(5) COPY() : to copy all those lines which contains ‘#’ to another file called “special.txt” , that is ,special.txt should contain only lines that contain ‘#’ as a character

(6) REPLACE() : write a function called replace () to replace a word with another user given word into another file called ‘duplicate.txt”.display both files

(7) DELETE( ): write a function called deleteword() , which deletes a given word in text file “POETIC.TXT”( hint : you need two files & add a space after each word)

(8)COUNTEND() :write a function called countend (), which counts the no. Of lines ending with the character ‘y’ or ‘i’. (do not take into consideration the case of the character

(9) VOWEL() :write a function called vowel() , which copies all words that starts with a vowel to another file called vowel.txt, display both the file content.

(10)CHANGE() :write a function called change() , that replaces every space with “**” and siplay both files .'''

import os

def create():
    file = open('POETIC.txt' , 'w')
    n = int(input('Enter the number of lines : '))
    for i in range (n):
        string = input('Enter the string : ')
        file.write(string + '\n')
    file.close()
    display()

def display():
    nof = input('Enter the full file name : ')
    file = open(nof , 'r')
    for i in file:
        print(i , end = '')
    file.close()


def countchar():
    nof = input('Enter the full file name : ')
    file = open(nof , 'r')
    count_upper = 0
    count_lower = 0
    count_consonent = 0
    count_vowel = 0
    for i in file:
        for j in i:
            if j in 'aeiouAEIOU':
                count_vowel += 1
                if j.isupper():
                    count_upper += 1
                elif j.islower():
                    count_lower += 1
            elif j in 'bcdfghjklmnopqrstvwxyzBCDFGHJKLMNOPQRSTVWXYZ':
                count_consonent  += 1
                if j.isupper():
                    count_upper += 1
                elif j.islower():
                    count_lower += 1

    print('The number of Vowels are --> ',count_vowel)
    print('The number of consonent are --> ',count_consonent)
    print('The number of uppercase are --> ',count_upper)
    print('The number of lowercase are --> ',count_lower)


def hashshow():
    file = open("POETIC.txt" , "r")
    for i in file:
        k = i.split()
        for j in k:
            print(j,end="#")
        print("\n")

def copy():
    nof = input('Enter file name : ')
    file = open(nof , 'r')
    filen = open('special.txt' , 'w')

    for i in file:
        k = i.split()
        for j in k:
            if j == '#':
                filen.write(i)
    file.close()
    display()

def replace():
    nof = input('Enter file name : ')
    file = open(nof , 'r')
    filen = open('duplicate.txt' , 'w')
    word_old = input('Enter the word to be deleted')
    word_new = input('Enter the word to replace with')

    for i in file:
        k = i.split()
        for j in k:
            if j != word_old:
                filen.write(j + ' ')
            else:
                filen.write(word_new+ ' ')
        filen.write('\n')
    file.close()
    filen.close()
    display()

def delete():
    nof = input('Enter file name : ')
    file = open(nof , 'r')
    filen = open('duplicate.txt' , 'w')
    word_del = input('Enter the word to be deleted')

    for i in file:
        k = i.split()
        for j in k:
            if j != word_del:
                filen.write(j + ' ')

        filen.write('\n')


    file.close()
    filen.close()
    os.remove('poetic.txt')
    os.rename('duplicate.txt','poetic.txt')
    display()

def countend():
    nof = input('Enter name of file : ')
    file = open(nof , 'r')
    count = 0
    for i in file:
        if i[-1] in "yi":
            count += 1
    print(count)
    file.close()
    display()

def vowel():
    nof = input('Enter the name of the file : ')
    file = open(nof , 'r')
    filen = open('vowel.txt' , 'w')

    for i in file:
        k = i.split()
        for j in k:
            if j[0] in 'aeiouAEIOU':
                filen.write(j+' ')
        filen.write('\n')
    file.close()
    filen.close()
    display()

def change():
    nof = input('Enter the full name of the file: ')
    file = open(nof , 'r')
    filen = open('chacharealsmooth.txt ' , 'w')
    for i in file:
        k = i.split()
        for j in k:
            filen.write(j+'**')
        filen.write('\n')
    file.close()
    filen.close()
    display()

while True:
    print('\n')
    print('''
(1) CREATE()

(2) DISPLAY

(3) COUNTCHAR

(4) HASHSHOW

(5) COPY

(6) REPLACE

(7) DELETE

(8)COUNTEND

(9) VOWEL

(10)CHANGE

(11)EXIT

''')
    option = int(input('Enter your choice : '))
    print('\n')

    if option == 1:
        create()
    elif option == 2:
        display()
    elif option == 3:
        countchar()
    elif option == 4:
        hashshow()
    elif option == 5:
        copy()
    elif option == 6:
        replace()
    elif option == 7:
        delete()
    elif option == 8:
        countend()
    elif option == 9:
        vowel()
    elif option == 10:
        change()
    elif option == 11:
        break
