import csv
import os

def create():
    n = int(input('Enter the number of lines'))
    with open('toy.csv' , 'w' , newline = '') as file:
        thewriter = csv.writer(file)
        for i in range(n):
            toyname = input('Enter the name of the toy')
            price = int(input('Enter the price of the toy'))
            cat = input('Enter the category')
            stk = int(input('Enter the stock'))
            thewriter.writerow([toyname,price,cat,stk])

def display():
    nof = input('Enter the name of the file:')
    with open(nof , 'r') as file:
        thereader = csv.reader(file)
        for i in thereader:
            print(i)

def search():
    name = input('Enter the name of the toy')
    with open('toy.csv' , 'r') as file:
        thereader = csv.reader(file)
        for i in thereader:
            if i[0] == name:
                print(i)
                break
        else:
            print('No such record found')

def append():
    n = int(input('Enter the number of lines'))
    with open('toy.csv' , 'a' , newline = '') as file:
        thewriter = csv.writer(file)
        for i in range(n):
            toyname = input('Enter the name of the toy')
            price = int(input('Enter the price of the toy'))
            cat = input('Enter the category')
            stk = int(input('Enter the stock'))
            thewriter.writerow([toyname,price,cat,stk])

def highest():
    with open('toy.csv' , 'r') as file:
        with open('highest.csv' , 'w' , newline = '') as filen:
            thereader = csv.reader(file)
            thewriter = csv.writer(filen)
            for i in thereader:
                if int(i[1]) > 100:
                    thewriter.writerow(i)
            print('Done...')

def modify():
    with open('toy.csv' , 'r') as file:
        with open('duplicate.csv' , 'w' , newline = '') as filen:
            thereader = csv.reader(file)
            thewriter = csv.writer(filen)
            for i in thereader:
                if int(i[3]) < 10:
                    stk = int(i[3]) + 10
                    thewriter.writerow([i[0],i[1],i[2],stk])
                else:
                    thewriter.writerow(i)
    os.remove('toy.csv')
    os.rename('duplicate.csv' , 'toy.csv')

def delete():
    with open('toy.csv' , 'r') as file:
        with open('duplicate.csv' , 'w' , newline = '') as filen:
            thereader = csv.reader(file)
            thewriter = csv.writer(filen)
            for i in thereader:
                if i[2] == 'fun':
                    pass
                else:
                    thewriter.writerow(i)
    os.remove('toy.csv')
    os.rename('duplicate.csv' , 'toy.csv')

#create()
while True:
    print('\n')
    print('''
1) CREATE
2) DISPLAY
3) SEARCH
4) APPEND
5) HIGHEST
6) MODIFY
7) DELETE
8) EXIT''')
    output = int(input('Enter choice'))
    if output == 1:
        create()
    elif output == 2:
        display()
    elif output == 3:
        search()
    elif output == 4:
        append()
    elif output == 5:
        highest()
    elif output == 6:
        modify()
    elif output == 7:
        delete()
    else:
        break















    
    
            
        
