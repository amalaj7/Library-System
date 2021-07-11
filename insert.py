from pymongo import MongoClient
# from MongoDB import mongoOperation

# to initialize a mongoClient
client = MongoClient(host="localhost", port=27017)

# to access the database 
db = client["Library_System"]


# collections
book_list = db.books

book = [{
			"BookId": "100",
			"Title": "The Alchemist",
			"AuthorName": "Paulo Coelho",
			"Publishers": "HarperCollins",
            "Genre": ["Fantasy" , "Quest", "Drama", "Adventure" ]
		},
		{
			"BookId": "101",
			"Title": "Wings of Fire",
			"AuthorName": "A. P. J. Abdul Kalam",
			"Publishers": "Indianbooks",
            "Genre": ["Biography", "Autobiography", "Fiction","Inspirational"]
		},
		{
			"BookId": "102",
			"Title": "The Key To Happiness",
			"AuthorName": "Meik Wiking",
			"Publishers": "Life",
            "Genre": ["Inspirational"]
		},
        {
			"BookId": "103",
			"Title": "Adventures of Tom Sawyer",
			"AuthorName": "Mark Twain",
			"Publishers": "Simon & Schuster",
            "Genre": ["Adventure" , "Bildungsroman"]
		},
        {
			"BookId": "104",
			"Title": "Alice in Wonderland",
			"AuthorName": "Lewis Carrol",
			"Publishers": "Macmillan Publisher",
            "Genre": ["Children's literature", "Fiction", "Fantasy","Literary Nonsense" ]
		},
        {
			"BookId": "105",
			"Title": "Time Machine",
			"AuthorName": "H G Wells",
			"Publishers": "Henry Holt and Company",
            "Genre": ["Fiction" ]
		},
        {
			"BookId": "106",
			"Title": "The Vicar of Wakefield",
			"AuthorName": "Oliver Goldsmith",
			"Publishers": "Collins of Salisbury ",
            "Genre": ["Comedy", "Satire", "Novel" ]
		},
        {
			"BookId": "107",
			"Title": "A Dangerous place",
			"AuthorName": "D.P. Moynihan",
			"Publishers": "HarperCollins Publishers",
            "Genre": ["Mystery", "Fiction" ]
		},
        {
			"BookId": "108",
			"Title": "Utopia",
			"AuthorName": "Sir Thomas Moor",
			"Publishers": "Client Publishers",
            "Genre": ["Fiction", "Satire" ]
		},
        {
			"BookId": "109",
			"Title": "The Merchant of Venice",
			"AuthorName": "Shakespeare",
			"Publishers": "Selina Publishers",
            "Genre": ["Comedy"]
		},
        {
			"BookId": "110",
			"Title": "Crime and Punishment",
			"AuthorName": "Dostoevsky",
			"Publishers": "The Russian Messenger",
            "Genre": ["Novel", "Manga", "Mystery", "Crime novel", "Fiction"]
		},
        {
			"BookId": "111",
			"Title": "King Lear",
			"AuthorName": "Shakespeare",
			"Publishers": "The Russian Messenger",
            "Genre": ["Comedy" ]
		},
        {
			"BookId": "112",
			"Title": "The Winner Stands Alone",
			"AuthorName": "Paulo Coelho",
			"Publishers": "HarperCollins",
            "Genre": ["Fantasy" ,"Quest", "Drama", "Adventure" ]
		}
        ]

result = book_list.insert_many(book)
print(result)


# book1 = {
#			"BookId": "113",	
# 			"Title": "Born a Crime",
# 			"AuthorName": "Trevor Noah",
# 			"Publishers": "Paramount Players",
#           "Genre": ["Humour", "Biography", "Autobiography" ]
# 		}
# mongoOperation.addSingleBook(book1)