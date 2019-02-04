import string
def stringoperation(lisofwords):
    myfile = open("royal-navy.txt","r")
    wordsl = open(lisofwords,"r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    newlist = []
    newwords = []
    for my in myfile:
        my = my.strip()
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        lis = my.split()
        for li in lis:
            listofwords.append(li)
    for lists in listofwords:
        if lists not in histo:
            histo[lists] = 1
        else:
            histo[lists] += 1
    for word in wordsl:
        word = word.strip()
        word = word.lower()
        newwords.append(word) 
    for key, value in histo.items():
        if key not in newwords:
            print(key)

x = input("Enter file name of list of words:")
stringoperation(x)



