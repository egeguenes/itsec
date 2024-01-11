import argparse

def main():
	parser = argparse.ArgumentParser(description='a script to find the private keys of the participants')

	parser.add_argument('-g', metavar='INT', type=int, help='generator of the key to exchange')
	parser.add_argument('-n', metavar='INT', type=int, help='modulus of the key to exchange')
	parser.add_argument('--alice', metavar='INT', type=int, help='alice public key')
	parser.add_argument('--bob', metavar='INT', type=int, help='bob public key')

	args = parser.parse_args()

	a_public_key = args.alice
	b_public_key = args.bob
	gen = args.g
	mod = args.n

	a_private_key, b_private_key = crack( mod , gen , a_public_key , b_public_key)

	print(pow( gen , a_private_key*b_private_key , mod))

def crack( n , g , a , b ): # n modulus // gen generator // a alice public key // b bob public key
	for i in range( 1 , n ):
		if pow( g , i , n ) == a:
			for j in range( 1 , n ): 
				if pow( g , j , n ) == b:
					return i, j
	return None, None



if __name__ == "__main__":
	main()