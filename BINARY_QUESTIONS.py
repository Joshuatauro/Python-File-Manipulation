import pickle
import os

def create():
  with open ("student.dat" , "wb") as file:
    n = int(input("Enter the number of entries : "))
    for i in range(0,n):
      roll = int(input("Enter the roll no : "))
      name = input("Enter the name : ")
      marks = int(input("Enter the marks : "))
      house = input("Enter the house")
      details = [roll,name,marks,house]
      pickle.dump(details,file)
  print("DONE")
  display("student.dat")

def display(nof):
  print("NOW SHOWING FILE "+nof)
  with open (nof , "rb") as file:
    try:
      while True:
        reader = pickle.load(file)
        print(reader)
    except EOFError:
      pass

def searchName():
  name = input("Enter the name : ")
  flag = 1
  with open ("student.dat" , "rb") as file:
    try:
      while True:
        reader = pickle.load(file)
        if reader[1] == name:
          flag = 2
          print(reader)
          break
        else:
          pass
    except EOFError:
      pass
  if flag == 1:
    print("No record found")

def append():
  with open ("student.dat" , "ab") as file:
    n = int(input("Enter the number of entries : "))
    for i in range(0,n):
      roll = int(input("Enter the roll no : "))
      name = input("Enter the name : ")
      marks = int(input("Enter the marks : "))
      house = input("Enter the house")
      details = [roll,name,marks,house]
      pickle.dump(details,file)
  print("DONE")
  display("student.dat")

def count():
  average = 0
  count = 0
  totalMarks = 0
  with open ("student.dat" , "rb") as file:
    try:
      while True:
        reader = pickle.load(file)
        count += 1
        totalMarks += reader[2]  
    except EOFError:
      pass
  print("THE TOTAL NUMBER OF ENTRIES ARE "+ str(count))
  print("THE AVERAGE MARKS IS "+str(totalMarks/count))

def highest():
  with open ("student.dat" , "rb") as file:
    with open ("high.dat" , "wb") as filen:
      try:
        while True:
          reader = pickle.load(file)
          if reader[2] > 85:
            pickle.dump(reader, filen)
          else:
            pass
      except EOFError:
        pass
  display("high.dat")

def modify():
  with open("student.dat" , "rb") as file:
    with open("imposter.dat" , "wb") as filen:
      try:
        while True:
          reader = pickle.load(file)
          if reader[2] < 23:
            marks = reader[2]+10
            item = [reader[0],reader[1],marks,reader[3]]
            pickle.dump(item,filen)
          else:
            pickle.dump(reader,filen)
      except EOFError:
        pass
  print("DONE")
  os.remove("student.dat")
  os.rename("imposter.dat" , "student.dat")
  display("student.dat")

def delete():
  with open ("student.dat" , "rb") as file:
    with open("imposter.dat" , "wb") as filen:
      try:
        while True:
          reader = pickle.load(file)
          if reader[-1] != "EMERALD":
            pickle.dump(reader, filen)
          else:
            pass
      except EOFError:
        pass
  print("DONE")
  os.remove("student.dat")
  os.rename("imposter.dat" , "student.dat")
  display("student.dat")

def deleteRoll():
  rollNo = int(input("Enter the roll no : "))
  with open ("student.dat" , "rb") as file:
    with open("imposter.dat" , "wb") as filen:
      try:
        while True:
          reader = pickle.load(file)
          if reader[0] != rollNo:
            pickle.dump(reader, filen)
          else:
            pass
      except EOFError:
        pass


  print("DONE")
  os.remove("student.dat")
  os.rename("imposter.dat" , "student.dat")
  display("student.dat")
while True:
  print('''
    1) CREATE
    2) DISPLAY
    3) SEARCHNAME
    4) COUNT
    5) HIGHEST
    6) MODIFY
    7) DELETE
    8) DELETEROLL
  ''')

  option = int(input("Enter the option : "))
  if option == 1:
    create()
  elif option == 2:
    nof = input("ENTER THE NAME OF THE FILE : ")
    display(nof)
  elif option == 3:
    searchName()
  elif option == 4:
    count()
  elif option == 5:
    highest()
  elif option == 6:
    modify()
  elif option == 7:
    delete()
  elif option == 8:
    deleteRoll()
  else:
    break