# vigenere cipher with arguments / decrypt encrypt out and a text file to do the operations

import argparse
import string

def main():
    parser = argparse.ArgumentParser(description='A tool to encrypt and decrypt a given message with the help of the key using the Vigenere cipher method')

    
    parser.add_argument('--encrypt', metavar='KEY', help='encrypts a message')
    parser.add_argument('--decrypt', metavar='KEY', help='decrypts a cipher')
    parser.add_argument('--out', metavar='OUTFILE', help='the encrypted text is to find in outfile')
    parser.add_argument('file', metavar='FILE', help='reads the ciphertext from file and decrypts it')   

    args = parser.parse_args()
    print("Arguments:", args)

    with open(args.file) as text:
        message = text.read()

    if args.encrypt:
        key = args.encrypt
    else:
        key = args.decrypt

    if args.encrypt:
        result = encrypt(message.lower(), key)
    else:
        result = decrypt(message, key)

    if args.out:
        with open(args.out , 'w') as outfile:
            outfile.write(result)
    else:
        print(result)


def encrypt(message, key):
    index = 0
    cipher = ""
    for c in message:
        if c in string.ascii_lowercase:
            overlap = ord(key[index]) - ord('a')
            cipher += chr((ord(c - ord('a') + overlap) % 26) + ord('a'))
            index = (index + 1) % len(key)
    return cipher

def decrypt(cipher , key):
	index = 0
	message = ""
	for c in cipher:
		if c in string.ascii_lowercase:
			overlap = (ord(key[index]) - ord(c)) % 26
			message += chr(overlap + ord('a'))
			index = (index + 1) % len(key)
	return message
