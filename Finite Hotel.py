n = int(input("> \n"))
m = int(input("> \n"))
x = int(input("> \n"))
listofprime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
dictionary = dict()

def hotelnumber_times2(n):
    global dictionary
    for i in range(n+1):
        dictionary[i] = i*2
    return dictionary

def hotelnumber_addm(m,n):
    global dictionary
    for i in range(n+1):
        dictionary[i] = i+m
    return dictionary

def hotelnumber_poweroftwo():
    for i in listofprime:
        dictionary[i] = i**2
    return dictionary

def hotelnumber_powerofx(x):
    for i in listofprime:
        sequence = list()
        for a in range(x+1):
            sequence.append(i**a)
        dictionary[i] = sequence
    return dictionary



print(hotelnumber_times2(n))
print(hotelnumber_addm(m,n))
print(hotelnumber_poweroftwo())
print(hotelnumber_powerofx(x))