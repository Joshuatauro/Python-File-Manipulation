import csv
import os

def create():
    with open ('student.csv' , 'w' , newline ='') as file:
        writer = csv.writer(file)
        n = int(input('Enter the number of lines'))
        for i in range (n):
            name = input('Enter student name :')
            engMarks = int(input('Enter English Marks: '))
            cscMarks = int(input('Enter Csc Marks : '))
            phyMarks = int(input('Enter Phy Marks : '))
            chemMarks = int(input('Enter Chem Marks : '))
            mathMarks = int(input('Enter Math Marks : '))
            average = (engMarks+cscMarks+mathMarks+phyMarks+chemMarks)//5

            details = [name , engMarks , cscMarks , phyMarks , chemMarks , mathMarks , average]

            writer.writerow(details)

def display():
    filen = input('Enter the file name : ')
    with open (filen , 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            print(i)

def search():
    name = input('Enter the student name')
    with open ('student.csv' , 'r') as file:
        reader = csv.reader(file)
        for i in reader:
            if i[0] == name:
                print(i)
                break
        else:
            print('Not found')

def append():
    with open ('student.csv' , 'a' , newline ='') as file:
        writer = csv.writer(file)
        n = int(input('Enter the number of lines'))
        for i in range (n):
            name = input('Enter student name :')
            engMarks = int(input('Enter English Marks: '))
            cscMarks = int(input('Enter Csc Marks : '))
            phyMarks = int(input('Enter Phy Marks : '))
            chemMarks = int(input('Enter Chem Marks : '))
            mathMarks = int(input('Enter Math Marks : '))
            average = (engMarks+cscMarks+mathMarks+phyMarks+chemMarks)//5

            details = [name , engMarks , cscMarks , phyMarks , chemMarks , mathMarks , average]

            writer.writerow(details)

def failure():
    with open ('student.csv' , 'r' , newline ='') as file:
        with open ('failure.csv' , 'w' , newline ='') as filen:
            reader = csv.reader(file)
            writer = csv.writer(filen)
            for i in reader:
                if int(i[1]) < 33 or int(i[2]) < 33 or int(i[3]) < 33 or int(i[4]) < 33 or int(i[5]) < 33:
                    writer.writerow(i)
                else:
                    pass
    print('Done')

def highest():
    with open('student.csv' , 'r') as file:
        with open('highest.csv' , 'w' , newline = '') as filen:
            reader = csv.reader(file)
            writer = csv.writer(filen)
            for i in reader:
                if int(i[6]) < 85:
                    writer.writerow(i)
                else:
                    pass
    print('Done')

def modify():
    with open('student.csv' , 'r') as file:
        with open('imposter.csv' , 'w' , newline = '') as filen:
            reader = csv.reader(file)
            writer = csv.writer(filen)
            for i in reader:
                if int(i[2]) < 50:
                    marks = int(i[2])
                    newMean = (int(i[1]) + marks+10 + int(i[3]) + int(i[4]) + int(i[5]))//5 
                    writer.writerow([i[0] , i[1] , marks+10 , i[3] , i[4] , i[5] , newMean])
                else:
                    writer.writerow(i)
    os.remove('student.csv')
    os.rename('imposter.csv' , 'student.csv')
    print('Done')

def delete():
    with open('student.csv' , 'r') as file:
        with open('imposter.csv' , 'w' , newline = '') as filen:
            reader = csv.reader(file)
            writer = csv.writer(filen)
            for i in reader:
                if int(i[-1]) < 40:
                    pass
                else:
                    writer.writerow(i)
                    
    os.remove('student.csv')
    os.rename('imposter.csv' , 'student.csv')
    print('Done')
   
create()
while True:
    print('''Please enter your choice
(1) CREATE()

(2) DISPLAY

(3) SEARCH

(4) APPEND

(5) FAILURE

(6) HIGHEST

(8)MODIFY

(9) DELETE

(10)EXIT

''')
    option = int(input('Enter your choice : '))
    print('\n')

    if option == 1:
        create()
    elif option == 2:
        display()
    elif option == 3:
        search()
    elif option == 4:
        append()
    elif option == 6:
        failure()
    elif option == 7:
        modify()
    elif option == 8:
        modify()
    elif option == 9:
        delete()
    elif option == 10:
        break
