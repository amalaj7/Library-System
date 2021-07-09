from pymongo import MongoClient
from functools import reduce

# to initialize a mongoClient
client = MongoClient(host="localhost", port=27017)

# to access the database 
db = client["Library_System"]


# collections
book_list = db.books

def addManyBooks(book):
	
	"""
	This function adds many documents in MongoDB
	"""

	try :
		client = MongoClient(host = "localhost",port = 27017)
		db = client['Library_System']
		book_list = db.books
		result = book_list.insert_many(book)
		print(result)

	except Exception as e :
		raise Exception("Error Occured in addManyBooks function :"+ str(e))
		

def addSingleBook(singleBook):
	
	"""
	This function add a single document in MongoDB
	"""

	try : 
		client = MongoClient(host = "localhost",port = 27017)
		db = client['Library_System']
		book_list = db.books
		result = book_list.insert_one(singleBook)
		print(result)

	except Exception as e :

		raise Exception("Error Occured in addSingleBook function :"+ str(e))

def collectionCreation(nameOfCollection):
	
	"""
	This function creates a new collection in the mongoDB but 
	a document needs to be inserted for it to create .
	"""

	try:
		client = MongoClient(host = "localhost",port = 27017)
		db = client['Library_System']
		mycol = db[nameOfCollection]
		print(mycol)

	except Exception as e:

		raise Exception("Error Occured in createCollection function :"+ str(e))


def dropCollection(collection_name):

	"""
	This Function drop the collections in MongoDB
	"""

	try:
		client = MongoClient(host="localhost", port=27017)
		db = client["Library_System"]
		mycol = db[collection_name]
		mycol.drop()
		print('Deleted Successfully')

	except Exception as e:

		raise Exception("Error Occured in dropCollection function :"+ str(e))


def UpdateCollection(existingKeyName,existingKeyValue,newKeyValue):
	"""
	This function updates the existing collection
	"""

	try:
		a = db.books.update({existingKeyName: existingKeyValue},{ "$set": { existingKeyName: newKeyValue}})
		print(a)

	except Exception as e:

		raise Exception("Error Occured in UpdateCollection function :"+ str(e))



def SearchbyBook(op):
	
	"""
	This function searches the Book by Title 
	Returns Author, Publishers, and Genres 
	"""

	try:

		list1 = []
		for a in book_list.find({"Title":{"$regex":op,"$options":"$i"}}):
			list1.append(a)
		return list1 

	except Exception as e:

		raise Exception("Error Occured in SearchByBook function :"+ str(e))
	

def SearchbyAuthor(op):

	"""
	This function searches the Book By Author Name
	Returns Book Name, Publisher and Genre

	"""
	
	try:

		list2 = []

		for a in book_list.find(({"AuthorName":{"$regex":op,"$options":"$i"}})):
			list2.append(a)
		return list2
		

	except Exception as e:

		raise Exception("Error Occured in SearchByAuthor function :"+ str(e))


def SearchbyGenre(op):

	"""
	This function searches the Genre of Book
	Returns Book Name , Author and Publisher 
	"""

	try:

		list3 = []
		for i in op:
			list4 = []
			for a in book_list.find({"Genre":{"$regex":i,"$options":"$i"}}):
				list4.append(a['Title'])
			list3.append(list4)

		res = list(reduce(lambda i, j: i & j, (set(x) for x in list3)))

		list5=[]
		for k in res:
			
			for a in book_list.find({"Title":{"$regex":k,"$options":"$i"}}):
				list5.append(a)
	
		return list5

	except Exception as e:

		raise Exception("Error Occured in SearchByGenre function :"+ str(e))
