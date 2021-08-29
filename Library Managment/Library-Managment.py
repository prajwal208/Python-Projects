#-------------------------------Library Management Project--------------------------

class library:
	def __init__(self, list):			#constructor
		self.booklist = list
		self.lendDict= {}

	def displayBook(self):
		for book in self.booklist:
			print(book)

	def lendBook(self, user, book):
		if book not in self.lendDict.keys():
			self.lendDict.update({book:user})
			print("Lender Book database has been updated")
		else:
			print("Book is already had be Taken")

	def add(self, book):
		self.booklist.append(book)
		print("Book has been succesfuly added to the List")

	def returnBook(self,book):
		self.lendDict.pop(book)
		print("Book has been succesfuly Returned to the List")


if __name__ == "__main__":
	Object = library(["Data Strcture","Python","Java","C++","C programming","C#","Java Script"])

	while True:
		print("---------------------------Library System--------------------------")
		print("1.Display Book")
		print("2.Lend Book")
		print("3.Add Book")
		print("4.Return Book")
		print("5.Exit")

		user_choice = input("Enter your Choice: ")
		if user_choice == "1":
			print("List of Books:")
			Object.displayBook()


		elif user_choice == "2":
			book = input("Enter the Book Name: ")
			user = input("Enter your Name: ")
			Object.lendBook(user,book)

		elif user_choice == "3":
			book = input("Enter the Book name to Add: ")
			Object.add(book)

		elif user_choice == "4":
			book = input("Enter the Book name to Return: ")
			Object.returnBook(book)
		
		elif user_choice == "5":
			break

		else:
			print("Inavlid Option")
				
			
			
			


				
				








	



		
			
		