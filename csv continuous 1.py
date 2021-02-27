'''CSV CONTINUOUS ASSIGNMENT'''

'''
 -(1)CREATE() : TO CREATE A “PRODUCT.CSV” FILE CONTAINING  N RECORDS HAVING THE FOLLOWING DETAILS :
    PROD ID
    NAME OF PRODUCT
    PRICE
    CATEGORY
    STOCK
WRITE ALL THESE DETAILS FOR EVERY RECORD INTO THE FILE
 -(2)DISPLAY(): TO DISPLAY THE CONTENTS OF THE FILE WHOSE FILE NAME IS INPUT BY THE USER
 -(3)SEARCHNAME(): TO SEARCH AND DISPLAY FOR GIVEN NAME AS INPUT BY THE USER , GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND.
 -(4)SEARCHID(): TO SEARCH AND DISPLAY FOR GIVEN ID AS INPUT BY THE USER , GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND.
 -(5)SEARCHPRICE(): TO SEARCH AND DISPLAY ALL PRODUCTS WHERE PRICE IS ABOVE 500, GIVE APPROPRIATE MESSAGE IF RECORD NOT FOUND.
 -(6) APPEND() : TO ADD ADDITIONAL ‘N’ RECORDS INTO “PRODUCT.CSV”.
 -(7)COUNT() : TO COUNT THE TOTAL NO.OF RECORDS IN THE  FILE.ALSO FIND THE SUM OF ALL THE STOCKS OF ALL PRODUCTS IN THE FILE
 -(8) HIGHEST(): TO COPY THE RECORDS OF PRODUCT  WHERE PRICE > 100  INTO ANOTHER FILE CALLED “HIGHEST.CSV”
 -(9)MODIFY() : TO MODIFY STOCK  OF THOSE PRODUCT WHERE STOCK IS LESS THAN 10 ,BY ADDING 10 TO THEIR EXISTING  STOCK.
 -(10)DELETE() : TO DELETE ALL PRODUCTS WHERE CATEGORY IS “FOOD” 
 -(11)DELETEID(): TO DELETE  PRODUCT WITH THE GIVEN USER DEFINED ID , GIVE APPROPRIATE MESSAGE IF PRODUCT NOT FOUND'''

import csv
import os

def create():
    n = int(input('Enter the number of entries'))
    with open ('product.csv' , 'w' , newline = '') as file:
        thewriter = csv.writer(file)
        for i in range(n):
            prod_id = int(input('Enter the prod id : '))
            nop = input('Enter the name of the product : ')
            price = int(input('Enter the price : '))
            cat = input('Enter the category : ')
            stk = int(input('Enter the stock : '))
            thewriter.writerow([prod_id,nop,price,cat,stk])

def display():
    nof = input('Enter the whole filen name : ')
    with open(nof , 'r') as file:
        thereader = csv.reader(file)
        for i in thereader:
            print(i)

def searchname():
    name = input('Enter the product name : ')
    flag = 0
    with open('product.csv' , 'r') as file:
        thereader = csv.reader(file)
        for i in thereader:
            if i[1] == name:
                print(i)
                flag = 1
    if flag == 0:
        print('Not found!')

def searchid():
    name = input('Enter the product id : ')
    flag = 0
    with open('product.csv' , 'r') as file:
        thereader = csv.reader(file)
        for i in thereader:
            if i[0] == name:
                print(i)
                flag = 1
    if flag == 0:
        print('Not found!')

def searchprice():
    name = input('Enter the product price : ')
    flag = 0
    with open('product.csv' , 'r') as file:
        thereader = csv.reader(file)
        for i in thereader:
            if i[2] == name:
                print(i)
                flag = 1
    if flag == 0:
        print('Not found!')

def append():
    n = int(input('Enter the number of entries'))
    with open ('product.csv' , 'a' , newline = '') as file:
        thewriter = csv.writer(file)
        for i in range(n):
            prod_id = int(input('Enter the prod id : '))
            nop = input('Enter the name of the product : ')
            price = int(input('Enter the price : '))
            cat = input('Enter the category : ')
            stk = int(input('Enter the stock : '))
            thewriter.writerow([prod_id,nop,price,cat,stk])

def count():
    row = 0
    stk = 0
    with open('product.csv' , 'r') as file:
        thereader = csv.reader(file)
        for i in thereader:
            row += 1
            stk += int(i[4])
    print('Total number of rows are -->' , row)
    print('Total stock is -->' , stk)
    
def highest():
    with open('product.csv' , 'r') as file:
        with open('highest.csv' , 'w' , newline = '') as filen:
            thereader = csv.reader(file)
            thewriter = csv.writer(filen)
            for i in thereader:
                print(i)
               # if int(i[2]) > 100:
                 #   thewriter.writerow(i)

def modify():
    with open('product.csv' , 'r') as file:
        with open('duplicate.csv' , 'w' , newline = '') as filen:
            thewriter = csv.writer(filen)
            thereader = csv.reader(file)
            for i in thereader:
                if int(i[4]) < 10:
                    k = int(i[4])+10
                    thewriter.writerow([i[0] , i[1] , i[2] , i[3] , k])
                else:
                    thewriter.writerow(i)
    os.remove('product.csv')
    os.rename('duplicate.csv' , 'product.csv')

def delete():
    with open('product.csv' , 'r') as file:
        with open('duplicate.csv' , 'w' , newline = '') as filen:
            thewriter = csv.writer(filen)
            thereader = csv.reader(file)
            for i in thereader:
                if i[3] != 'Food':
                    thewriter.writerow(i)
    os.remove('product.csv')
    os.rename('duplicate.csv' , 'product.csv')
