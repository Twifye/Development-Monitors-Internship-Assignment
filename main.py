from movie_manager import add_movie, update_tickets, book_ticket, list_movies


def menu():
    while True:
        print("\nMovie Ticket System")
        print("1. Add Movie")
        print("2. Update Ticket Count")
        print("3. Book a Ticket")
        print("4. List Movies")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter movie title: ")
            tickets = int(input("Enter number of tickets: "))
            add_movie(title, tickets)

        elif choice == "2":
            title = input("Enter movie title: ")
            count = int(input("Enter number of tickets to add: "))
            update_tickets(title, count)

        elif choice == "3":
            title = input("Enter movie title: ")
            book_ticket(title)

        elif choice == "4":
            list_movies()

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()
