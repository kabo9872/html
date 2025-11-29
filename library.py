class library:
    def __init__(self,list,name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library:  {self.name}")
        for book in self.bookList :
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")

        else:
            print(f"Book is alreadyy being used by {self.lendDict[book]}")    
    
    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':

    books = library(['Python','Rich Dad Poor Dad','Harry Potter','Car Basics','Algorithms By CLRS'], "lETS uPSKILL")

    while(True):
        print(f"Welcom to the {books.name} library. Enter your choice to continue")
        print("1. display books")
        print("2. lend a book")
        print("3. add a book")
        print("4. return a book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
            continue


        else:
            user_choice = int(user_choice)

        
        if user_choice == 1:
            books.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you ant to lend")
            user = input("Enter name")
            books.lendBook(user, book)  

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            books.addBook(book)  

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            books.returnBook(book)
        
        else:
            print("Not a valid option")

        
        print("press q to quit and c to continue")
        user_choise2 = ""
        while(user_choise2!="c" and user_choise2!="q"):
            user_choise2 = input()
            if user_choise2 == "q":
                exit()
            
            elif user_choice2 == "c":
                continue

        

            

        


