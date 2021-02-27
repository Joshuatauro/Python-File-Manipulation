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
        print(i, end = '')
    file.close()

def counthe():
    file = open('ABC.txt' , 'r')
    count = 0
    for i in file:
        k = i.split()
        for j in k:
            if j == 'he':
                count += 1
    print(count)
    file.close()

def vowelwords():
    file = open('ABC.txt' , 'r')
    filen = open('vowel.txt' , 'w')
    for i in file:
        k = i.split()
        for j in k:
            if j[0] in 'aeiouAEIOU':
                filen.write(j+'\n')
    print('Done')
    file.close()
    filen.close()

def replace():
    delw = input('Enter the word to be deleted')
    deln = input('Enter the word to replace it with')
    file = open('abc.txt' , 'r')
    filen = open('duplicate.txt' , 'w')
    for i in file:
        k = i.split()
        for j in k:
            if j == delw:
                filen.write(deln+' ')
            else:
                filen.write(j+' ')
        filen.write('\n')
    file.close()
    filen.close()

def delword():
    delw = input('Enter the word to be deleted')
    file = open('ABC.txt' , 'r')
    filen = open('duplicate.txt' , 'w')
    for i in file:
        k = i.split()
        for j in k:
            if j != delw:
                filen.write(j+' ')
        filen.write('\n')
    file.close()
    filen.close()

def now():
    count = 0
    file = open('ABC.txt' , 'r')
    for i in file:
        k = i.split()
        for j in k:
            if (len(j) == 4) and (j[0] == 'T'):
                count += 1
                print(j)
    print(count)
    file.close()

def test():
    f=open("abc.txt")
    f.seek(7)
    txt=f.read(3)
    print(txt)
    lines=f.readlines()
    print(len(lines))


