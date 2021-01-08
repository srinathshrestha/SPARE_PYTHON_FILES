class Library:
    def __init__(self,book_list,librarian):
        self.book_list=book_list
        self.name=librarian
        self.lend_dict ={}

    def view_book(self):
        for i in self.book_list:
            print(i)

    def lend_book(self,user,book):
        if book  not in self.lend_dict.keys():
            self.lend_dict.update({book: user})
            print(f"you can now take the book {book}")
        else:

            print(f"sorry!! Book is already being used by {self.lend_dict[book]}")
    def donate_book(self,book):
        self.book_list.append(book)
    def return_book(self,book):
        self.lend_dict.pop(book)


if __name__ == '__main__':

    srinath = Library(['Secret Seven on the Trail', 'Everything is fucked', 'Stories we never tell', 'RICH DAD POOR DAD',
                 'Benjamin Franklin', 'Merchants of Doubt', 'Life 3.0', 'Pack Update', 'The Road Ahead',
                 'Cutting Through Spiritual Materialism'],'SRINATH')

    while (True):
        print(f"This is {srinath.name}'s library. Enter your choice to continue : ")
        print("1. View Books")
        print("2. Lend a Book")
        print("3. Donate a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            srinath.view_book()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend :")
            user = input("Enter your name : ")
            srinath.lend_book(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add :")
            srinath.donate_book(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return :")
            srinath.return_book(book)

        else:
            print("Not a valid option")

        print("\nPress q to quit and c to continue : ")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                print(f'Thanks for visiting {srinath.name} librabry')
                exit()

            elif user_choice2 == "c":
                continue
