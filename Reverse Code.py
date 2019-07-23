input1 = str(input("Masukan kata yang diinginkan: \n"))

def reverse_encrypt(input1):
    x = 0
    word = input1
    for i in input1:
        i = input1[-(x+1)]
        word = word[:x] + i + word[x+1:]
        x += 1
    return word

print(reverse_encrypt(input1))