a = input(">")
b = input(">")
c = input(">")

def find(word,letter,start):
    index = int(start)
    while index < len(word):
        if word[index] == letter:
            return index
        index+=1
    return -1


def count(word,char):
    count=0
    for i in word:
        if i == char :
            count+=1
    return count