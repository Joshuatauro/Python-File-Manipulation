"""Write a function filter(oldfile, newfile) that copies all the lines of a text file “source.txt”
onto “target.txt” except those lines which starts with “@” sign."""

def filter(oldfile, newfile):
  file = open(oldfile, 'r')
  filen = open(newfile, 'w')

  for i in file:
    if i[0] != '@':
      filen.write(i)
    
  file.close()
  filen.close()

def display(name):
  file = open(name , 'r')
  for i in file:
      print(i , end = '')

file = open('source.txt', 'w')
file.write('@helo world \n')
file.write('helo my name is joshua \n')
file.write('wassup up lads my name is joshua \n')
file.close()

display('source.txt')

filter('source.txt', 'target.txt')
