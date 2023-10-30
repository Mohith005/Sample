#1
'''

def create():
    f = open("prac1.txt","w")
    x = "Neither apple nor pine are in pineapple.Boxing rings are square.\nWriters write, but fingers don't fing.Overlook and oversee are opposites.\nA house can burn up as it burns down. An alarm goes off by going on."
    f.write(x)

    f.close()

create()
print()

def read1():
    f = open('prac1.txt' , 'r')
    x = f.read()
    print(x)

    f.close

read1()
print()

def addmore():
   
    f = open('prac1.txt' , 'a')
    x = input("Add more? (y/n):")
    if x == 'y':
        y = input("Enter: ")
        f.write('\n'+y)

    else :
        pass
   
    f.close()

    f1 = open('prac1.txt' , 'r')
    l = f1.readlines()
    n = len(l)
    for i in range(n):
        print(i+1,".",l[i])

    f.close()
   
addmore()
print()

def last():
    f = open("prac1.txt" , 'r')
    l = f.readlines()
    print("The last line is: ",l[-1])

    f.close()

last()
print()

def specific():
    f = open("prac1.txt" , 'r')
    x = f.readlines()
    f.seek(10)
    l = f.readlines()
    print(l[0])

    f.close()

specific()
print()

def line():
    f = open("prac1.txt" , 'r')
    x = f.readlines()
    print("No. of lines are",len(x))
    n = int(input("Enter which line to print: "))
    print(x[n-1])

    f.close()

line()
print()


def frequency():
    f = open("prac1.txt" , 'r')
    x = f.read().lower()
    l = x.split()
    
    d = {}
    for i in l:
        z = i[0]
        if z not in d:
            d[z]=1

        elif z in d:
            d[z]+=1

    d = dict(sorted(d.items()))
    n = len(d)
    for i in d:
        v = d[i]
        print("Words beginning with",i,":",v)

     
    f.close()

frequency()
'''

#2

def isvowel():
    print("hi")
    f = open("prac1.txt",'r')
    x = f.read().lower()
    l = x.split()
    n = []

    for i in l:
        if i[0] in "aeiou":
            continue
        else:
            n = n+[i]

    print(n)
    f.close()

    f1 = open("2.txt",'w')
    for i in n:
        f1.write(i+" ")

    f1.close()
   
isvowel()


#4

d = {}
def histogram():
    f = open("mytext.txt" , 'r')
    x = f.read().lower()
    l = x.split()
    
    global d
    for i in l:
        x = i.isalpha()
        if x == False:
            continue

        else:
            if i not in d:
                d[i]=1

            elif i in d:
                d[i]+=1


    total = len(l)
    diff = len(d)
    print("Total number of words: ",total)
    print("Number of different words: ",diff)

    print()
    f.close()

    
def find_longest_word():
        
    keys = d.keys()
    minimum = 0
    for j in keys:
        if minimum < len(j):
            minimum = len(j)
            longest = j

        else:
            continue

    print("The longest word present is:",longest)
    print()


def filter_long_words(n):
    
    keys = d.keys()
    l = []
    minimum = n
    for j in keys:
        if minimum < len(j):
            l = l + [j]

        else:
            continue

    print("The longest word present is:",l)

n = int(input("Enter any integer: "))


histogram()
find_longest_word()
filter_long_words(n)
    
'''

#9


def romanToInt(s):
    d = { "I":1,"V":5,"X":10,"l":50,"C":100,"D":500,"M":1000 }
    


'''




s = input("Enter: ")
romanToInt(s)










          

