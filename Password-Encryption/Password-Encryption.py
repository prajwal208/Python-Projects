from cryptography.fernet import Fernet

print("-------------------------------Password Manager----------------------------")

'''def writeKey():				#togenerate Key
	key = Fernet.generate_key()
	with open("key.key","wb") as key_file:
		key_file.write(key)
writeKey()'''

def loadKey():
	file = open("key.key","rb")
	key = file.read()
	file.close()
	return key


key = loadKey()
fer = Fernet(key)

def view():
	with open("password.txt", "r") as fle:
		for line in fle.readlines():
			data = line.rstrip()
			user,password = data.split('||')
			print("userName:",user," || userPassword: ", fer.decrypt(password.encode()).decode())


def add():
	userName = input("Enter UserName: ")
	userPassword = input("Enter Password: ")
	with open ("password.txt",'a') as fle:				#a -> append file
		fle.write("UserName: " + userName + " || " + "Password: " + fer.encrypt(userPassword.encode()).decode()+ "\n")

while True:
	print("Note: Press q for quit")
	userMode= input("Would you like to add new Password || View exseting Password (press add/view): ").lower() 
	if userMode == 'q':
		break	

	if userMode == 'add':
		add()
	elif userMode == 'view':
		view()
	else:
		print("Invalid Input")
		continue











