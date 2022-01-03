def enkripsi(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def dekripsi(chipertext, key):
    return enkripsi(chipertext, key)

def main():
    print("Pilih: \n1. Enkripsi Text \n2. Dekripsi Text")
    pilih = int(input("Pilihan: "))

    if pilih == 1:
        plaintext = str(input("Input plaintext: "))
        key = str(input("Input key: "))

        print("Plaintext: ", plaintext)
        print("Hasil Enkripsi: ", enkripsi(plaintext, key))
    elif pilih == 2:
        chipertext = str(input("Input chipertext: "))
        key = str(input("Input key: "))

        print("Chipertext: ", chipertext)
        print("Hasil Dekripsi: ", dekripsi(chipertext, key))

main()