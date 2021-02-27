"""Write a function AMCount() in Python, which should read each character of a text
file STORY.TXT, should count and display the occurrence of alphabets A and M
(including small cases a and m too).
Example:
If the file content is as follows:
 Updated information
 As simplified by official websites.
The AMCount() function should display the output as:
A or a:4"""

def write():
  file = open('STORY.txt', 'w')
  file.write("Updated information As simplified by official websites.")

def AMCount():
  count = 0
  file = open('STORY.txt', 'r')
  for i in file:
    for j in i:
      if j in 'AaMm':
        count += 1
  file.close()
  print('THE NUMBER OF TIMES A,M APPEAR IS => ', count)

write()
AMCount()