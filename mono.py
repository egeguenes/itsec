# a script to encrypt and dexrypt a message or a text with commands, also can give the output as a file or as system.out

import argparse

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def encrypt(message, key):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            char = key[ord(char.lower()) - ord('a')]
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ''
    for char in encrypted_message:
        if char.isalpha():
            char = chr(key.index(char) + ord('a'))
            decrypted_message += char
    return decrypted_message

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a message using a monoalphabetic substitution cipher.')
    parser.add_argument('--encrypt', metavar='KEY', help='Encrypt the message using the specified key alphabet')
    parser.add_argument('--decrypt', metavar='KEY', help='Decrypt the message using the specified key alphabet')
    parser.add_argument('--out', dest='outfile', metavar='OUTFILE', help='Specify the output file. If not specified, write to standard output')
    parser.add_argument('file', metavar='FILE', help='Input file containing the message')

    args = parser.parse_args()

    if args.encrypt:
        key = args.encrypt
        action = encrypt
    elif args.decrypt:
        key = args.decrypt
        action = decrypt
    else:
        parser.error('Either --encrypt or --decrypt must be specified')

    if len(key) != 26 or len(set(key)) != 26:
        parser.error('The key must be a string containing each character of the alphabet a-z exactly once')

    message = read_file(args.file)
    result = action(message, key)

    if args.outfile:
        write_file(args.outfile, result)
    else:
        print(result)

if __name__ == "__main__":
    main()
