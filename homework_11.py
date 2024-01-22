# This program will encrypt your text file into a new file using the Caesar's cipher.

import argparse
import string

parser = argparse.ArgumentParser(description = "This program will encrypt your text file into a new file using the Caesar's cipher.")
parser.add_argument('input', type = str, help = 'Enter the name and/or path to the file, you want to encrypt.')
parser.add_argument('output', type = str, help = 'Enter the name and/or path which will specify the newly created enrypted file.')
parser.add_argument('--shift', type = int, default = 21, help = "Enter a number by which you want to shift the alphabet ecryption in the Caesar's cipher")
parser.add_argument('--both', action = 'store_true', help = "If True, the output file will include the original text as well as the ecrypted one.")

def encrypt_file(input_file, output_file, n, both_texts = False):
    alphabet_lowercase = string.ascii_lowercase
    alphabet_uppercase = string.ascii_uppercase
    caesar_cypher = dict(zip(alphabet_lowercase, alphabet_lowercase[n-1:] + alphabet_lowercase[:n-1]))
    caesar_cypher.update(dict(zip(alphabet_uppercase, alphabet_uppercase[n-1:] + alphabet_uppercase[:n-1])))

    with open(input_file, mode='r', encoding = 'utf-8') as file_to_encrypt:
        content = file_to_encrypt.read()
        with open(output_file, mode='w', encoding = 'utf-8') as encrypted_file: 
            content_encrypted = '' 
            for letter in content:
                for key in caesar_cypher:
                    if letter.lower() not in alphabet_lowercase:
                        content_encrypted += letter
                        break
                    if letter == key:
                        content_encrypted += caesar_cypher[key]
                        break
            if both_texts:
                encrypted_file.write(content + 2*"\n")
            encrypted_file.write(content_encrypted)

args = parser.parse_args()
encrypt_file(args.input, args.output, args.shift, args.both)    
