def encryption(word, shift):
    result = ""

    for i in range(len(word)):
        char = word[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def decryption(word, shift):
    result = ""

    for i in range(len(word)):
        char = word[i]

        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


# check the above function
text = "DEFENDTHEFORT"
s = 7

encrypt = encryption(text, s)
decrypt = decryption(encrypt, s)

print("Original text: ", text)
print("Encrypted: ", encrypt)
print("Decrypted: ", decrypt)

print("Added new line from github")
print("Added new line from laptop")
