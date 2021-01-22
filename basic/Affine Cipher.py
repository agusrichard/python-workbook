plain_text = str(input("Masukan teks yang diinginkan:\n"))
a = int(input("Masukan kunci a: \n"))
b = int(input("Masukan kunci b: \n"))
alphabet = "abcdefghijklmnopqrstuvwxyz"
# the value of a must be chosen such that a and m are coprime

def encrypt_affine_cipher(plain_text,a,b):
    x = 0
    for i in plain_text:
        index = 0
        while index < len(alphabet):
            if i == alphabet[index]:
                while x < len(plain_text):
                    if plain_text[x] == i:
                        plain_text = plain_text[:x] + alphabet[(index*a + b) % 26] + plain_text[x + 1:]
                        x += 1
                        break
            if i == " ":
                plain_text = plain_text[:x] + " " + plain_text[x + 1:]
                x += 1
                break
            index += 1
    return (plain_text)

print(encrypt_affine_cipher(plain_text,a,b))