from MongoDB import mongoOperation

print('Welcome to Library Management System')
print('-----------------------------------------')
print('\n')

print('Press 1 for Selecting Books by name')
print('------------------------------------------')
print('Press 2 for Selecting Books by Author name')
print('------------------------------------------')
print('Press 3 for Selecting Similar Tags of Genre')
print('------------------------------------------')
print('Press 4 for Updating Existing Collection')
print('\n')

def userChoice():

    choice = int(input("Enter your choice : "))

    if choice == 1:

        option = input("Enter the name of the book : ")
        print('\n')
        out = mongoOperation.SearchbyBook(option)
        for i in out:
            print('These are the books with its details')
            print('--------------------------------------')

            print("Author : {aname}, Publisher : {pub}, Genre : {gen}".format(aname = i["AuthorName"], pub = i['Publishers'], gen = i['Genre']))

    elif choice == 2:

        option = input("Enter the name of the author : ")
        print('\n')
        out = mongoOperation.SearchbyAuthor(option)
        print('These are the books with the Same Author ')
        for i in range(len(out)):
            j = out[i]
            print('--------------------------------------')
            print(i+1 ,",","Book Name : {fname}, Publisher : {pub}, Genre : {gen}".format(fname = j['Title'], pub = j['Publishers'], gen = j['Genre'])) 

    elif choice == 3:

        option = input("Enter the genre : ")
        print('\n')
        option = option.split(' ')
        option = [i.lower().strip() for i in option]
        print('Genre : ',option)
        out = mongoOperation.SearchbyGenre(option)
        print('These are the books with the Same Genres/Tags')
        
        for i in range(len(out)):
            j = out[i]
            print('--------------------------------------')
            
            print(i+1 ,",", "Book Name : {fname}, Author : {aname}, Publisher : {pub}".format(fname = j["Title"], aname = j["AuthorName"], pub = j['Publishers'])) 

    else:
        op1 =input("Enter the Key Name: ")
        op2 = input("Enter the Key Value: ")
        op3 =input("Enter the New Value: ")
        out = mongoOperation.UpdateCollection(op1, op2, op3)
        print(out, "\n Successfully updated")



if __name__ == "__main__":
    userChoice()