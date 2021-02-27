import csv
import os

def create():
     with open ("student.csv" , 'w', newline="") as file:
          thewriter = csv.writer(file)
          # thewriter.writerow(["NAME","E_MARKS","MATH_MARKS","PHY_MARKS","CHEM_MARKS","CS_MARKS","AVERAGE"])
          n = int(input('Enter the number of inputs :'))
          for i in range(0,n):
               name = input('Enter name')
               e_marks = int(input('Enter english'))
               cs_marks = int(input("Enter cs"))
               math_marks = int(input("Enter maths"))
               phy_marks = int(input("Enter phy"))
               ch_marks = int(input("Enter chem"))
               average = (e_marks+cs_marks+math_marks+phy_marks+ch_marks)//5
               details = [name,e_marks,math_marks,phy_marks,ch_marks,cs_marks,average]
               thewriter.writerow(details)
     display("student.csv")

def display(nof):
     print("READING FROM FILE "+nof)
     with open(nof, 'r', newline="") as file:
          reader=csv.reader(file)
          print(["NAME","E_MARKS","MATH_MARKS","PHY_MARKS","CHEM_MARKS","CS_MARKS","AVERAGE"])
          for i in reader:
               print(i)
          print("\n")

def search():
     name = input("Enter the name")
     with open("student.csv" , 'r') as file:
          reader = csv.reader(file)
          for i in reader:
               if i[0] == name:
                    print(i)
                    break
          else:
               print("None found")
               print("\n")

def append():
     n = int(input("Enter the number fo entries = "))
     with open ("student.csv" , 'a' , newline="") as file:
          writer = csv.writer(file)
          for i in range(0,n):
               name = input('Enter name')
               e_marks = int(input('Enter english'))
               cs_marks = int(input("Enter cs"))
               math_marks = int(input("Enter maths"))
               phy_marks = int(input("Enter phy"))
               ch_marks = int(input("Enter chem"))
               average = (e_marks+cs_marks+math_marks+phy_marks+ch_marks)//5
               details = [name,e_marks,math_marks,phy_marks,ch_marks,cs_marks,average]
               writer.writerow(details)
     print("\n")
     display("student.csv")

def failure():
     with open("fail.txt" , "w", newline="") as file:
          with open ("student.csv" , "r") as filen:
               reader = csv.reader(filen)
               writer = csv.writer(file)
               for i in reader:
                    if int(i[-1]) < 33:
                         writer.writerow(i)
     print("Done")
     display("fail.txt")
     
def highest():
     with open("highest.csv" , "w", newline="") as file:
          with open ("student.csv", "r") as filen:
               reader = csv.reader(filen)
               writer = csv.writer(file)
               for i in reader:
                    if int(i[-1]) > 85:
                         writer.writerow(i)
                    else:
                         pass
     print("Done")
     display("highest.csv")


def modify():
     with open ("imposter.csv" , "w", newline="") as file:
          with open("student.csv" , "r") as filen:
               reader = csv.reader(filen)
               writer = csv.writer(file)
               for i in reader:
                    if int(i[5]) < 50:
                         cs_marks = int(i[5])+10
                         item = [i[0] , i[1], i[2] , i[3] , i[4] , cs_marks,  i[6]]
                         writer.writerow(item)
                    else:
                         writer.writerow(i)
     
     os.remove("student.csv")
     os.rename("imposter.csv" , "student.csv")
     print("DONE")
     display("student.csv")

def delete():
     with open ("student.csv" , "r") as file:
          with open ("imposter.csv" , "w" , newline="") as filen:
               reader = csv.reader(file)
               writer = csv.writer(filen)
               for i in reader:
                    if int(i[-1]) > 45:
                         writer.writerow(i)
                    else:
                         pass
     print("DONE")
     os.remove("student.csv")
     os.rename("imposter.csv" , "student.csv")
     display("student.csv")



while True:
     print('''
     1) CREATE
     2) DISPLAY
     3) SEARCH
     4) APPEND
     5) FAILURE
     6) HIGHEST
     7) MODIFY
     8) DELETE
     ''')

     option = int(input("Enter option = "))
     if option == 1:
          create()
     elif option == 2:
          nof = input("Enter the name of the file = ")
          display(nof)
     elif option == 3:
          search()
     elif option == 4:
          append()
     elif option == 5:
          failure()
     elif option == 6:
          highest()
     elif option == 7:
          modify()
     elif option == 8:
          delete()
     else:
          print("Breaking")
          break