# Alice uses the RSA algorithm for encrypting a message m. Her public key (exponent) is 211 with modulus 67063
# ciphertext c = 19307

# Encrypt message m to ciphertext c = m^e mod n
# Decrypt ciphertext c to message m = c^d mod n
# choose a random p q and their multiplication and (p-1)*(q-1) and a number corpime to it and thats key e // e * d = 1 mod(p*q -p -q +1)

# pow(c,d) = pow(m, e * d) = m * pow(m, k * (p-1) * (q-1)) = m // mod n

#public key = 211, finde eine fi funktion, die mit 211 coprime ist, dann mach pow(c , d , mod), dann bekommst du die nachricht, ed = 1 mod fi funktion, c =m^e mod n

import argparse
import math

def main():
	parser = argparse.ArgumentParser(description='rsa cracking script')
	parser.add_argument('-e', metavar='INT', type=int, help='exponent integer') 			 # public key e
	parser.add_argument('-n', metavar='INT', type=int, help='modulus integer')				 # modulus
	parser.add_argument('--ciphertext', metavar='INT', type=int, help='ciphertext to crack') # c
	args = parser.parse_args()

	exp = args.e 			 # öffentliche exponente "e"
	mod = args.n
	c_text = args.ciphertext

	my_list = lister(mod)

	for i in my_list:
		for j in my_list:
			fi = (i-1) * (j-1)
			



def prime_list(num):
	 if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def lister(num):
	my_list = [2]
	for i in range(3,num):
		my_list.append(i)
	return my_list

def rsa_crack(c , d , n):
	cracked_int = pow(c , d , n)
	return cracked_int

if __name__ == "__main__":
	main()