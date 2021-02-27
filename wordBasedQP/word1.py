"""Write a method/function ISTOUPCOUNT() in python to read contents from a text file
WRITER.TXT, to count and display the occurrence of the word ‘‘IS’’ or ‘‘TO’’ or ‘‘UP’’.
 For example : If the content of the file isIT IS UP TO US TO TAKE CARE OF OUR SURROUNDING. IT IS NOT POSSIBLE
ONLY FOR THE GOVERNMENT TO TAKE RESPONSIBILITY
The method/function should display Count of IS TO and UP is 6"""

def write():
  file = open('writer.txt','w')
  file.write('If the content of the file isIT IS UP TO US TO TAKE CARE OF OUR SURROUNDING. IT IS NOT POSSIBLE ONLY FOR THE GOVERNMENT TO TAKE RESPONSIBILITY')
    

def ISTOUPCOUNT():
  file = open('writer.txt','r')
  count = 0
  for i in file:
    k = i.split()
    for j in k:
      if j in ['IS', 'TO', 'UP']:
        count +=1
  file.close()
  print('The number of times IS TO UP appeared in the string is =>', count)


write()
ISTOUPCOUNT()

