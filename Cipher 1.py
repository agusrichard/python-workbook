plain_text = str(input("Masukan teks yang diinginkan: \n"))
keyword = str(input("Masukan kata kunci yang diinginkan: \n"))
alphabet = "abcdefghijklmnopqrstuvwxyz "

def encrypt_cipher1(plain_text,keyword):
    counter_for_y = 0
    i = 0
    new_plain_text = plain_text
    for x in plain_text:
        index_plaintext = 0
        while index_plaintext < len(alphabet):
            if x == alphabet[index_plaintext]:
                store1 = index_plaintext
                break
            index_plaintext += 1
        index_keyword = 0
        y = keyword[counter_for_y]
        while index_keyword < len(alphabet):
            if y == alphabet[index_keyword]:
                store2 = index_keyword
                break
            index_keyword += 1
        code_number = (store1+store2) % 27
        code_char = alphabet[code_number]
        new_plain_text = new_plain_text[:i] + code_char + new_plain_text[i + 1:]
        i += 1
        counter_for_y += 1
        if counter_for_y > len(keyword)-1:
            counter_for_y = 0
    return(new_plain_text)

def decrypt_cipher1(plain_text,keyword):
    counter_for_y = 0
    i = 0
    new_plain_text = plain_text
    for x in plain_text:
        index_plaintext = 0
        while index_plaintext < len(alphabet):
            if x == alphabet[index_plaintext]:
                store1 = index_plaintext
                break
            index_plaintext += 1
        index_keyword = 0
        y = keyword[counter_for_y]
        while index_keyword < len(alphabet):
            if y == alphabet[index_keyword]:
                store2 = index_keyword
                break
            index_keyword += 1
        code_number = (store1 - store2)
        if code_number < 0:
            store1 = store1 + 27
            code_number = store1 - store2
        code_char = alphabet[code_number]
        new_plain_text = new_plain_text[:i] + code_char + new_plain_text[i + 1:]
        i += 1
        counter_for_y += 1
        if counter_for_y > len(keyword) - 1:
            counter_for_y = 0
    return (new_plain_text)


print(encrypt_cipher1(plain_text,keyword))