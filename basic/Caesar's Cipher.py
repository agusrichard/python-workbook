input1 = str(input("Masukan kata yang diinginkan: \n"))
key = int(input("Masukan kunci yang diinginkan: \n"))
alphabet = "abcdefghijklmnopqrstuvwxyz"

def word_index(input1):
    for i in input1:
        index = 0
        while index < len(alphabet):
            if i == alphabet[index]:
                print(alphabet[index])
            index += 1

def caesar_code_1(input1,key):
    for i in input1:
        index = 0
        while index < len(alphabet):
            if i == alphabet[index]:
                print(alphabet[index+key])
            index += 1

def caesar_encrypt(input1,key):
    x = 0
    for i in input1:
        index = 0
        while index < len(alphabet):
            if i == alphabet[index]:
                while x < len(input1):
                    if input1[x] == i:
                        input1 = input1[:x] + alphabet[(index + key) % 26] + input1[x + 1:]
                        x += 1
                        break
            if i == " " :
                input1 = input1[:x] + " " + input1[x + 1:]
                x += 1
                break
            index += 1
    return(input1)

def caesar_decrypt(input1,key):
    x = 0
    for i in input1:
        index = 0
        while index < len(alphabet):
            if i == alphabet[index]:
                while x < len(input1):
                    if input1[x] == i:
                        input1 = input1[:x] + alphabet[(index - key) % 26] + input1[x + 1:]
                        x += 1
                        break
            if i == " ":
                input1 = input1[:x] + " " + input1[x + 1:]
                x += 1
                break
            index += 1
    return(input1)

print(caesar_encrypt(input1,key))
print(caesar_decrypt(caesar_encrypt(input1,key),key ))