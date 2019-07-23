text = str(input("Masukan teks yang diinginkan: \n"))

def histogram(text):
    dictionary = dict()
    for i in text:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary

def listing_histogram(dictionary):
    list_histogram = list()
    for x in dictionary:
        list_histogram.append(x)
    list_histogram.sort()
    return list_histogram

def print_histogram(dictionary):
    for x in dictionary:
        print(x,dictionary[x])

def ordered_print_histogram(dictionary):
    list_histogram = list()
    for x in dictionary:
        list_histogram.append(x)
    list_histogram.sort()
    for i in range(len(list_histogram)):
        print(list_histogram[i],dictionary[list_histogram[i]])

def inverse_dictionary(dictionary):
    inverse = dict()
    for key in dictionary:
        value = dictionary[key]
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    return inverse
