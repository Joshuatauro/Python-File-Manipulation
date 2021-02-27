import pickle
import os

def create():
    with open('student.dat' , 'wb') as file:
        n = int(input('Enter the number of lines'))
        for i in range (n):
            roll = int(input('Enter the roll no'))
            nos = input('Enter name of student')
            marks = int(input('Enter marks'))
            house = input('Enter house')
            details = [roll , nos , marks , house]

            pickle.dump(details,file)

def display():
    nof = input('Enter full file name')
    with open(nof , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                print(r)
        except EOFError:
            pass

def searchName():
    name = input('Enter name of student to find : ')
    with open ('student.dat' , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                if r[1] == name:
                    print(r)
                    break
        except EOFError:
            print('No result')

def searchId():
    identity =int(input('Enter id of student to find : '))
    with open ('student.dat' , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                if r[0] == identity:
                    print(r)
                    break
        except EOFError:
            print('No result')

def append():
    with open('student.dat' , 'ab') as file:
        n = int(input('Enter the number of lines'))
        for i in range (n):
            roll = int(input('Enter the roll no'))
            nos = input('Enter name of student')
            marks = int(input('Enter marks'))
            house = input('Enter house')
            details = [roll , nos , marks , house]

            pickle.dump(details,file)

def count():
    number = 0
    totalSum = 0
    with open('student.dat' , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                number += 1
                totalSum += r[2]
        except EOFError:
            pass
    print('The number of entries are',number)
    print('The average marks is ',totalSum/number)
                
def high():
    with open('student.dat' , 'rb') as file:
        with open ('high.dat' , 'wb') as filen:
            try:
                while True:
                    r = pickle.load(file)
                    if r[2] > 90:
                        pickle.dump(r , filen)
            except EOFError:
                pass
    print('Done')

def modify():
    with open('student.dat' , 'rb') as file:
        with open ('imposter.dat' , 'wb') as filen:
            try:
                while True:
                    r = pickle.load(file)
                    if r[2] < 23:
                        details = [r[0] , r[1] , r[2]+10 , r[3]]
                        pickle.dump(details,filen)
                    else:
                        pickle.dump(r,filen)
            except EOFError:
                pass
    os.remove('student.dat')
    os.rename('imposter.dat' , 'student.dat')
    
def deleteHouse():
    with open('student.dat' , 'rb') as file:
        with open ('imposter.dat' , 'wb') as filen:
            try:
                while True:
                    r = pickle.load(file)
                    if r[3] != 'Emerald':
                        pickle.dump(r , filen)
            except EOFError:
                pass
    print('Done')
    os.remove('student.dat')
    os.rename('imposter.dat' , 'student.dat')

def deleteRoll():
    rollNumber = int(input('Enter the roll number : '))
    with open('student.dat' , 'rb') as file:
        with open ('imposter.dat' , 'wb') as filen:
            try:
                while True:
                    r = pickle.load(file)
                    if r[0] != rollNumber:
                        pickle.dump(r , filen)
            except EOFError:
                pass
    print('Done')
    os.remove('student.dat')
    os.rename('imposter.dat' , 'student.dat')
    

while True:
    print('''Please enter your choice
(1) CREATE()

(2) DISPLAY

(3) SEARCHNAME

(4) SEARCHID

(5) APPEND

(6) COUNT

(7) HIGHEST

(8)MODIFY

(9) DELETE

(10)DELETEROLL

(11)EXIT

''')
    option = int(input('Enter your choice : '))
    print('\n')

    if option == 1:
        create()
    elif option == 2:
        display()
    elif option == 3:
        searchName()
    elif option == 4:
        searchId()
    elif option == 5:
        append()
    elif option == 6:
        count()
    elif option == 7:
        high()
    elif option == 8:
        modify()
    elif option == 9:
        deleteHouse()
    elif option == 10:
        deleteRoll()
    elif option == 11:
        break
