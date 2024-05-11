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
