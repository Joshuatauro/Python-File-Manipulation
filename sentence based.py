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

def countlines():
    file = open('ABC.txt')
    count = 0
    for i in file:
        if i[0] in 'Aa':
            count += 1
    print(count)
    file.close()

def reverse():
    file = open('abc.txt' , 'r')
    filen = open('reverse.txt' , 'w')
    for i in file:
        k = i[-1::-1]
        filen.write(k)
    file.close()
    filen.close()

def vowelline():
    file = open('abc.txt' , 'r')
    filen = open('duplicate.txt' , 'w')
    for i in file:
        if i[0] in 'aeiouAEIOU':
            filen.write(i)
    file.close()
    filen.close()

def big():
    file = open('abc.txt')
    great = 0
    for i in file:
        large = i
        k = len(i)
        if k > large:
            large = len(i)

def noc():
    file = open('abc.txt')
    filen = open('duplicate.txt' , 'w')
    for i in file:
        if i[0] not in 'Cc':
            filen.write(i)
    file.close()
    filen.close()
            
            
        
        
