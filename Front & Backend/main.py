import tkinter as tk
from tkinter import messagebox
import psycopg2
from config import config

# Establish database connection
db_connection = psycopg2.connect(
    host="localhost",
    database="Library_Management_System",
    user="postgres",
    password="2354232"
)

# Function to connect to the database
def connect():
    connection = None
    try:
        params = config()
        print('Connection to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        print('PostgreSQL database version:')
        cursor = connection.cursor()
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')

# Function to add a book to the database
def add_book():
    add_book_window = tk.Toplevel()
    add_book_window.title("Add Book")

    def add_book_to_db():
        try:
            book_title = title_entry.get()
            author = author_entry.get()
            edition = int(edition_entry.get())
            copies = int(copies_entry.get())

            cursor = db_connection.cursor()
            cursor.execute("INSERT INTO books (title, author, edition, copies) VALUES (%s, %s, %s, %s)",
                           (book_title, author, edition, copies))
            db_connection.commit()
            messagebox.showinfo("Success", "Book added successfully.")
            add_book_window.destroy()
        except (psycopg2.Error, ValueError) as error:
            messagebox.showerror("Error", f"Error while adding book: {error}")

    tk.Label(add_book_window, text="Title:").grid(row=0, column=0)
    title_entry = tk.Entry(add_book_window)
    title_entry.grid(row=0, column=1)

    tk.Label(add_book_window, text="Author:").grid(row=1, column=0)
    author_entry = tk.Entry(add_book_window)
    author_entry.grid(row=1, column=1)

    tk.Label(add_book_window, text="Edition:").grid(row=2, column=0)
    edition_entry = tk.Entry(add_book_window)
    edition_entry.grid(row=2, column=1)

    tk.Label(add_book_window, text="Copies:").grid(row=3, column=0)
    copies_entry = tk.Entry(add_book_window)
    copies_entry.grid(row=3, column=1)

    add_button = tk.Button(add_book_window, text="Add Book", command=add_book_to_db)
    add_button.grid(row=4, columnspan=2, pady=5)

    add_book_window.mainloop()

# Function to issue a book to a user
def issue_book():
    issue_book_window = tk.Toplevel()
    issue_book_window.title("Issue Book")

    def issue_book_to_user():
        try:
            user_regno = int(user_regno_entry.get())
            book_id = int(book_id_entry.get())
            issue_date = issue_date_entry.get()

            cursor = db_connection.cursor()
            cursor.execute("INSERT INTO transactions (user_regno, book_id, transaction_type, transaction_date, returned) VALUES (%s, %s, %s, %s, FALSE)",
                           (user_regno, book_id, 'issue', issue_date))
            db_connection.commit()
            messagebox.showinfo("Success", "Book issued successfully.")
            issue_book_window.destroy()
        except (psycopg2.Error, ValueError) as error:
            messagebox.showerror("Error", f"Error while issuing book: {error}")

    tk.Label(issue_book_window, text="User Registration Number:").grid(row=0, column=0)
    user_regno_entry = tk.Entry(issue_book_window)
    user_regno_entry.grid(row=0, column=1)

    tk.Label(issue_book_window, text="Book ID:").grid(row=1, column=0)
    book_id_entry = tk.Entry(issue_book_window)
    book_id_entry.grid(row=1, column=1)

    tk.Label(issue_book_window, text="Issue Date (YYYY-MM-DD):").grid(row=2, column=0)
    issue_date_entry = tk.Entry(issue_book_window)
    issue_date_entry.grid(row=2, column=1)

    issue_button = tk.Button(issue_book_window, text="Issue Book", command=issue_book_to_user)
    issue_button.grid(row=3, columnspan=2, pady=5)

    issue_book_window.mainloop()

# Function to submit a book
def submit_book():
    submit_book_window = tk.Toplevel()
    submit_book_window.title("Submit Book")

    def submit_book_from_user():
        try:
            user_regno = int(user_regno_entry.get())
            book_id = int(book_id_entry.get())
            return_date = return_date_entry.get()

            cursor = db_connection.cursor()
            cursor.execute("UPDATE transactions SET returned = TRUE WHERE user_regno = %s AND book_id = %s AND transaction_type = 'issue'",
                           (user_regno, book_id))
            db_connection.commit()
            messagebox.showinfo("Success", "Book submitted successfully.")
            submit_book_window.destroy()
        except (psycopg2.Error, ValueError) as error:
            messagebox.showerror("Error", f"Error while submitting book: {error}")

    tk.Label(submit_book_window, text="User Registration Number:").grid(row=0, column=0)
    user_regno_entry = tk.Entry(submit_book_window)
    user_regno_entry.grid(row=0, column=1)

    tk.Label(submit_book_window, text="Book ID:").grid(row=1, column=0)
    book_id_entry = tk.Entry(submit_book_window)
    book_id_entry.grid(row=1, column=1)

    tk.Label(submit_book_window, text="Return Date (YYYY-MM-DD):").grid(row=2, column=0)
    return_date_entry = tk.Entry(submit_book_window)
    return_date_entry.grid(row=2, column=1)

    submit_button = tk.Button(submit_book_window, text="Submit Book", command=submit_book_from_user)
    submit_button.grid(row=3, columnspan=2, pady=5)

    submit_book_window.mainloop()

# Function to delete a book from the database
def delete_book():
    delete_book_window = tk.Toplevel()
    delete_book_window.title("Delete Book")

    def delete_book_from_db():
        try:
            book_id = int(book_id_entry.get())

            cursor = db_connection.cursor()
            cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
            db_connection.commit()
            messagebox.showinfo("Success", "Book deleted successfully.")
            delete_book_window.destroy()
        except (psycopg2.Error, ValueError) as error:
            messagebox.showerror("Error", f"Error while deleting book: {error}")

    tk.Label(delete_book_window, text="Book ID to delete:").grid(row=0, column=0)
    book_id_entry = tk.Entry(delete_book_window)
    book_id_entry.grid(row=0, column=1)

    delete_button = tk.Button(delete_book_window, text="Delete Book", command=delete_book_from_db)
    delete_button.grid(row=1, columnspan=2, pady=5)

    delete_book_window.mainloop()

# Function to display all books in the library
def display_books():
    display_books_window = tk.Toplevel()
    display_books_window.title("Display Books")

    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        books_text = ""
        for book in books:
            books_text += f"Book ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nEdition: {book[3]}\nCopies: {book[4]}\n------------------------\n"

        display_label = tk.Label(display_books_window, text=books_text)
        display_label.pack()
    except psycopg2.Error as error:
        messagebox.showerror("Error", f"Error while displaying books: {error}")

    display_books_window.mainloop()

# Function to display issued books with user details
def display_issued_books():
    display_issued_books_window = tk.Toplevel()
    display_issued_books_window.title("Issued Books")

    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT books.title, user_details.user_name, user_details.email FROM transactions INNER JOIN books ON transactions.book_id = books.book_id INNER JOIN user_details ON transactions.user_regno = user_details.user_regno WHERE transactions.transaction_type = 'issue' AND transactions.returned = FALSE")
        issued_books = cursor.fetchall()

        issued_books_text = ""
        for book in issued_books:
            issued_books_text += f"Title: {book[0]}\nIssued to: {book[1]}\nEmail: {book[2]}\n------------------------\n"

        display_label = tk.Label(display_issued_books_window, text=issued_books_text)
        display_label.pack()
    except psycopg2.Error as error:
        messagebox.showerror("Error", f"Error while displaying issued books: {error}")

    display_issued_books_window.mainloop()

# Function to add a user to the database
def add_user():
    add_user_window = tk.Toplevel()
    add_user_window.title("Add User")

    def add_user_to_db():
        try:
            user_regno = user_regno_entry.get()
            user_name = user_name_entry.get()
            email = email_entry.get()

            cursor = db_connection.cursor()
            cursor.execute("INSERT INTO user_details (user_regno, user_name, email) VALUES (%s, %s, %s)",
                           (user_regno, user_name, email))
            db_connection.commit()
            messagebox.showinfo("Success", "User added successfully.")
            add_user_window.destroy()
        except (psycopg2.Error, ValueError) as error:
            messagebox.showerror("Error", f"Error while adding user: {error}")

    tk.Label(add_user_window, text="User Registration Number:").grid(row=0, column=0)
    user_regno_entry = tk.Entry(add_user_window)
    user_regno_entry.grid(row=0, column=1)

    tk.Label(add_user_window, text="Name:").grid(row=1, column=0)
    user_name_entry = tk.Entry(add_user_window)
    user_name_entry.grid(row=1, column=1)

    tk.Label(add_user_window, text="Email:").grid(row=2, column=0)
    email_entry = tk.Entry(add_user_window)
    email_entry.grid(row=2, column=1)

    add_button = tk.Button(add_user_window, text="Add User", command=add_user_to_db)
    add_button.grid(row=3, columnspan=2, pady=5)

    add_user_window.mainloop()

# Function for student menu
def student_menu():
    student_window = tk.Tk()
    student_window.title("Student Menu")

    issue_button = tk.Button(student_window, text="Issue Book", command=issue_book)
    issue_button.pack(pady=5)

    submit_button = tk.Button(student_window, text="Submit Book", command=submit_book)
    submit_button.pack(pady=5)

    display_button = tk.Button(student_window, text="Display Books", command=display_books)
    display_button.pack(pady=5)

    back_button = tk.Button(student_window, text="Back", command=student_window.destroy)
    back_button.pack(pady=5)

    student_window.mainloop()

# Function for admin menu
def admin_menu():
    admin_window = tk.Tk()
    admin_window.title("Admin Menu")

    add_user_button = tk.Button(admin_window, text="Add User", command=add_user)
    add_user_button.pack(pady=5)

    display_books_button = tk.Button(admin_window, text="Display Books", command=display_books)
    display_books_button.pack(pady=5)

    add_book_button = tk.Button(admin_window, text="Add Book", command=add_book)
    add_book_button.pack(pady=5)

    delete_book_button = tk.Button(admin_window, text="Delete Book", command=delete_book)
    delete_book_button.pack(pady=5)

    issued_books_button = tk.Button(admin_window, text="Issued Books", command=display_issued_books)
    issued_books_button.pack(pady=5)

    back_button = tk.Button(admin_window, text="Back", command=admin_window.destroy)
    back_button.pack(pady=5)

    admin_window.mainloop()

# Function for main menu
def main_menu():
    main_window = tk.Tk()
    main_window.title("Main Menu")

    student_button = tk.Button(main_window, text="Student", command=student_menu)
    student_button.pack(pady=5)

    admin_button = tk.Button(main_window, text="Admin", command=admin_menu)
    admin_button.pack(pady=5)

    exit_button = tk.Button(main_window, text="Exit", command=main_window.destroy)
    exit_button.pack(pady=5)

    main_window.mainloop()

# Start the program
if __name__ == "__main__":
    connect()  # Establish database connection
    main_menu()  # Display main menu
