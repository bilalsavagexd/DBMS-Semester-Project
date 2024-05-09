import psycopg2
from config import config

# Establish database connection
db_connection = psycopg2.connect(
    host="localhost",
    database="Library_Management_System",
    user="postgres",
    password="2354232"
)

def connect ():
    connection = None
    try:
        params = config ()
        print ('Connection to the postgresSQL database...')
        connection = psycopg2.connect (**params)

# Creating a cursor
        crsr = connection.cursor ()
        print ('PostgresSQL database version: ')
        crsr.execute ('SELECT version ()')
        db_version = crsr.fetchone ()
        print (db_version)
        crsr.close ()
    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
    finally:
        if connection is not None:
            connection.close ()
            print ('Database connection Terminated')
if __name__ == "__main__":
    connect ()

# Function to add a book to the database
def add_book():
    try:
        book_title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        edition = int(input("Enter Edition: "))
        copies = int(input("Enter Copies: "))
        
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO books (title, author, edition, copies) VALUES (%s, %s, %s, %s)",
                       (book_title, author, edition, copies))
        db_connection.commit()
        print("Book added successfully.")
    except (psycopg2.Error, ValueError) as error:
        print("Error while adding book:", error)

# Function to issue a book to a user
def issue_book():
    try:
        user_regno = int(input("Enter User Registration Number: "))
        book_id = int(input("Enter Book ID: "))
        issue_date = input("Enter Issue Date (YYYY-MM-DD): ")
        
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO transactions (user_regno, book_id, transaction_type, transaction_date) VALUES (%s, %s, %s, %s)",
                       (user_regno, book_id, 'issue', issue_date))
        db_connection.commit()
        print("Book issued successfully.")
    except (psycopg2.Error, ValueError) as error:
        print("Error while issuing book:", error)

# Function to submit a book
def submit_book():
    try:
        user_regno = int(input("Enter User Registration Number: "))
        book_id = int(input("Enter Book ID: "))
        return_date = input("Enter Return Date (YYYY-MM-DD): ")
        
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO transactions (user_regno, book_id, transaction_type, return_date) VALUES (%s, %s, %s, %s)",
                       (user_regno, book_id, 'return', return_date))
        db_connection.commit()
        print("Book submitted successfully.")
    except (psycopg2.Error, ValueError) as error:
        print("Error while submitting book:", error)

# Function to delete a book from the database
def delete_book():
    try:
        book_id = int(input("Enter Book ID to delete: "))
        
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
        db_connection.commit()
        print("Book deleted successfully.")
    except (psycopg2.Error, ValueError) as error:
        print("Error while deleting book:", error)

# Function to display all books in the library
def display_books():
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        
        for book in books:
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Edition:", book[3])
            print("Copies:", book[4])
            print("------------------------")
    except psycopg2.Error as error:
        print("Error while displaying books:", error)

# Function for the main menu
def main_menu():
    while True:
        print("\nLIBRARY MANAGER")
        print("1. ADD BOOK")
        print("2. ISSUE BOOK")
        print("3. SUBMIT BOOK")
        print("4. DELETE BOOK")
        print("5. DISPLAY BOOKS")
        print("6. EXIT")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            issue_book()
        elif choice == '3':
            submit_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            display_books()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program by calling the main menu
if __name__ == "__main__":
    main_menu()
