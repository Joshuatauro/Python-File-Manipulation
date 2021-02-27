def create():
    n = input('Enter the name of the file')
    file = open(n , 'w')
    num = int(input('Enter the num of lines'))
    for i in range(num):
        s = input('Enter the line')
        file.write(s+'\n')
    file.close()

def display():
    name = input('Enter the file name')
    file = open(name , 'r')
    for i in file:
        print(i , end = '')

def countvowel():
    file = open('ABC.txt' , 'r')
    count = 0
    for i in file:
        for j in i:
            if j in 'aeiouAEIOU':
                count += 1
    print(count)

def counta():
    file = open('ABC.txt' , 'r')
    count = 0
    for i in file:
        for j in i:
            if j in 'Aa':
                count += 1
    print(count , 'is the number of times the word "a" appeared')

def copy():
    file = open('ABC.txt' , 'r')
    filen = open('DUPLICATE.txt' , 'w')
    for i in file:
        for j in i:
            filen.write(j)
    print('Done')
            
def change():
    file = open('ABC.txt' , 'r')
    filen = open('DUPLICATE.txt' , 'w')
    
    for i in file:
        for j in i:
            if j.islower():
                filen.write(j.upper())
            else:
                filen.write(j.lower())
    print('Done')

def star():
    file = open('ABC.txt' , 'r')
    filen = open('DUPLICATE.txt' , 'w')
    for i in file:
        for j in i:
            if j == ' ':
                filen.write('**')
            else:
                filen.write(j)
