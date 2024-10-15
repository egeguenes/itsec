import parser

def main():
	get_arguments()


def get_arguments():
	while True:
		parser = argparse.ArgumentParser(description="Diffie Hellman key exchange")
		parser.add_argument("-g" , type=int, help="generator number")
		parser.add_argument("-n" , type=int, help="modulo number")
		parser.add_argument("--a", type=int, help="alice secret key number")
		parser.add_argument("--b", type=int, help="bob secret key number")
		args = parser.parse_args()
		alice_secret = args.a
		bob_secret = args.b
		gen = args.g
		mod = args.n

		if alice_secret and bob_secret and gen and mod:
			break
		print("All arguments must be provided and non-zero!")
	use_arguments(alice_secret , bob_secret , gen , mod)

def pow_mod(number , gen , mod):
	return (gen ** number) % mod

def use_arguments(alice_secret , bob_secret , gen , mod):
	alice_public = pow_mod(alice_secret , gen , mod)
	bob_public = pow_mod(bob_secret , gen , mod)
	key = (alice_public ** bob_public) % mod
	print(key)

if __name__ == "__main__":
	main()