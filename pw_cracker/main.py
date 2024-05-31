import hashlib

# converts texts to the sha1 by firstly encoding the text and then using the hash algorithm and with hexdigest we get the encoded hex decimal nums
def convert_text_to_sha1(text):
	digest = hashlib.sha1(text.encode()).hexdigest()
	return digest

def main():
	user_sha1 = input("Enter the SHA1 to crack : ")

	# without the spaces and with lowercase this is the given sha1
	cleaned_user_sha1 = user_sha1.strip().lower()

	# open the file passwords.txt
	with open('./passwords.txt') as f:

		# iterate thru each password
		for line in f:
			password = line.strip()

			# password is converted to sha1
			converted_sha1 = convert_text_to_sha1(password)

			# when a converted password matches the given sha1 from the user -> output that password and kill the programm
			if cleaned_user_sha1 == converted_sha1:
				print(f"Password found : {password}")
				return

	print("Password not found!")

if __name__ == '__main__':
	main()