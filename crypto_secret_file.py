from cryptography.fernet import Fernet

def generate_key():
	key = Fernet.generate_key()
	with open("secret.key", "wb") as key_file:
		key_file.write(key)
	print("Key has created and saved in 'secret.key'")

def load_key():
	return open("secret.key", "rb").read()

def encrypt_file(filename):
	key = load_key()
	f = Fernet(key)

	with open(filename, "rb") as file:
		file_data = file.read()

	encrypted_data = f.encrypt(file_data)

	with open(filename + ".locked", "wb") as file:
		file.write(encrypted_data)
	print(f"File {filename} has encrypted!")

generate_key()
encrypt_file("password.txt")
