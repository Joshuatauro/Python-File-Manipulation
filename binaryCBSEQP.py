"""A binary file “Book.dat” has structure [BookNo, Book_Name, Author, Price].
i. Write a user defined function CreateFile() to input data for a
record and add to Book.dat .
ii. Write a function CountRec(Author) in Python which accepts the
Author name as parameter and count and return number of
books by the given Author are stored in the binary file
“Book.dat” """
import pickle

def CreateFile(n):
  with open('book.dat','wb') as file:
    for i in range(n):
      bookNo = int(input('Enter the book number'))
      bookName = input('Enter the book name')
      author = input('Enter the name of the author')
      price = int(input('Enter the price of the book'))
      pickle.dump([bookNo,bookName,author,price],file)


def countRec(author):
  authorCount = 0
  with open ('book.dat','rb') as file:
    try:
      while True:
        fileContent = pickle.load(file)
        if fileContent[2] == author:
          authorCount += 1
    except EOFError:
      pass
  print('The number of books this author has published is => ', authorCount)


CreateFile(3)
countRec('Joshua')
