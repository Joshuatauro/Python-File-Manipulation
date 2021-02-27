import pickle
import os

def create():
    n = int(input('Enter the num of records :'))
    with open('EMP.dat' , 'wb') as file:
        d = {}
        for i in range(n):
            d['eid'] = int(input('Enter eid : '))
            d['ename'] = input('Enter name : ')
            d['esal'] = int(input('Enter sal : '))
            d['edesig'] = input('Enter designation')
            day = int(input('Enter day'))
            m = int(input('Enter month'))
            y = int(input('Enter year'))
            d['doj'] = [day , m , y]
            pickle.dump(d , file)


def display():
    n = input('Enter file name')
    with open(n , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                print(r)
        except EOFError:
            pass


def append():
    n = int(input('Enter the num of records :'))
    with open('EMP.dat' , 'ab') as file:
        d = {}
        d['eid'] = int(input('Enter eid : '))
        d['ename'] = input('Enter name : ')
        d['esal'] = int(input('Enter sal : '))
        d['edesig'] = input('Enter designation')
        day = int(input('Enter day'))
        m = int(input('Enter month'))
        y = int(input('Enter year'))
        d['doj'] = [day , m , y]
        pickle.dump(d , file)


def searchid():
    flag = 0
    n = int(input('Enter the search id :'))
    with open('EMP.dat' , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                if r['eid'] == n:
                    print(r)
                    print('found')
                    flag = 10
        except EOFError:
            pass
        if flag == 0:
            print('not found')


def searchname():
    flag = 0
    name = input('Enter the name of the user')
    with open('EMP.dat' , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                if r['ename'] == name:
                    print(r)
                    flag = 10
                    print('found')
        except EOFError:
            pass
        if flag == 0:
            print('not found')
def searchmonth():
    count = 0

    month = int(input('Enter the month'))
    with open ('EMP.dat' , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                if r['doj'][1] == month:
                    print(r)
                    count += 1
        except EOFError:
            pass
        print(count , 'is the number of employees who joined in the month of ', month)
        
def copy():
    with open('EMP.dat' , 'rb') as file:
        with open('manger.dat' , 'wb') as filen:
            try:
                while True:
                    r = pickle.load(file)
                    if r['edesig'] == 'Manager':
                        pickle.dump(r , filen)


            except EOFError:
                pass
                    

def modifysal():
    with open('EMP.dat' , 'rb') as file:
        try:
            while True:
                r = pickle.load(file)
                if r['esal']<3000:
                    r['esal'] += 500         
        except EOFError:
            pass

            

def deleteid():
    k=int(input("enter id to be found"))
    flag = 10
    with open("emp.dat","rb")as r:
        with open("id.dat","wb",)as p:
            try:
                while True:
                    a = pickle.load(r)
                    if a["eid"]==k:
                        print("deleted")
                        flag = 100
                    else:
                        pickle.dump(a,p)
            except EOFError:
                pass
    if a==10:
        print("NOT FOUND")
    os.remove("emp.dat")
    os.rename("id.dat","emp.dat")
    
def deletedes():
    k=input("enter des to be found")
    flag = 10
    with open("emp.dat","rb")as r:
        with open("desig.dat","wb",)as p:
            try:
                while True:
                    a = pickle.load(r)
                    if a["edesig"]==k:
                        print("deleted")
                        flag = 100
                    else:
                        pickle.dump(a,p)
            except EOFError:
                pass
    if flag == 10:
        print("NOT FOUND")
    os.remove("emp.dat")
    os.rename("desig.dat","emp.dat")

create()
while True:
    print('\n')
    print("1) display")
    print("2) append")
    print("3) searchid")
    print("4) searchname")
    print("5) deleteid")
    print("6) modifysal")
    print("7) copy")
    print("8) deletdes")
    print("9) searchmonth")
    print("10) exit")
    print('\n')
    a=int(input("option"))
    if a==1:
        display()
    if a==2:
        append()
    if a==3:
        searchid()
    if a==4:
        searchname()
    if a==5:
        deleteid()
    if a==6:
        modifysal()
    if a==7:
        copy()
    if a==8:
        deletedes()
    if a==9:
        searchmonth()
    elif a == 10:
        break
