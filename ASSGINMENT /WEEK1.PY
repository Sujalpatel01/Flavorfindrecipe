import os

FILE_NAME = "books.txt"


def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{book_id},{book_name},{author}\n")

    print("Book Added Successfully")


def view_book():
    if not os.path.exists(FILE_NAME):
        print("No Book Record Found")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No Books Available")
        return

    print("\n========== BOOK RECORD ==========")

    for line in data:
        book = line.strip().split(",")

        print("Book ID :", book[0])
        print("Book Name :", book[1])
        print("Author :", book[2])
        print("-" * 30)


def search_book():
    search_id = input("Enter Book ID to Search: ")
    found = False

    if not os.path.exists(FILE_NAME):
        print("No Record Found")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            book = line.strip().split(",")

            if book[0] == search_id:
                found = True

                print("\nBook Found")
                print("Book ID :", book[0])
                print("Book Name :", book[1])
                print("Author :", book[2])

    if not found:
        print("Book Not Found")


def update_book():
    update_id = input("Enter Book ID to Update: ")

    if not os.path.exists(FILE_NAME):
        print("No Record Found")
        return

    new_data = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            book = line.strip().split(",")

            if book[0] == update_id:
                found = True

                new_name = input("Enter New Book Name: ")
                new_author = input("Enter New Author Name: ")

                new_data.append(
                    f"{update_id},{new_name},{new_author}\n"
                )
            else:
                new_data.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(new_data)

    if found:
        print("Book Updated Successfully")
    else:
        print("Book Not Found")


def remove_book():
    remove_id = input("Enter Book ID to Remove: ")

    if not os.path.exists(FILE_NAME):
        print("No Record Found")
        return

    new_data = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            book = line.strip().split(",")

            if book[0] == remove_id:
                found = True
            else:
                new_data.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(new_data)

    if found:
        print("Book Removed Successfully")
    else:
        print("Book Not Found")


def main():
    while True:
        print("\nLIBRARY MANAGEMENT :")
        print("\nADD BOOK")
        print("VIEW BOOK")
        print("UPDATE BOOK")
        print("SEARCH BOOK")
        print("REMOVE BOOK")
        print("EXIT")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_book()

        elif choice == "3":
            update_book()

        elif choice == "4":
            search_book()

        elif choice == "5":
            remove_book()

        elif choice == "6":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


main()