import tkinter as tk
from tkinter import messagebox
import psycopg2

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Establish database connection
        self.db_connection = psycopg2.connect(
            host="localhost",
            database="Library_Management_System",
            user="postgres",
            password="2354232"
        )

        # Create main menu frame
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame.pack()

        # Add buttons for Student and Admin functionalities
        self.student_button = tk.Button(self.main_menu_frame, text="Student", command=self.show_student_menu)
        self.student_button.grid(row=0, column=0, padx=10, pady=5)

        self.admin_button = tk.Button(self.main_menu_frame, text="Admin", command=self.show_admin_menu)
        self.admin_button.grid(row=0, column=1, padx=10, pady=5)

        self.exit_button = tk.Button(self.main_menu_frame, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def execute_query(self, query, params=None):
        try:
            cursor = self.db_connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.db_connection.commit()
            cursor.close()
        except psycopg2.Error as error:
            messagebox.showerror("Error", f"Database error: {error}")

    def show_student_menu(self):
        self.clear_buttons()

        self.display_books_button = tk.Button(self.main_menu_frame, text="Display Books", command=self.display_books_window)
        self.display_books_button.grid(row=2, column=0, padx=10, pady=5)

        self.issue_book_button = tk.Button(self.main_menu_frame, text="Issue Book", command=self.issue_book_window)
        self.issue_book_button.grid(row=2, column=1, padx=10, pady=5)

        self.submit_book_button = tk.Button(self.main_menu_frame, text="Submit Book", command=self.submit_book_window)
        self.submit_book_button.grid(row=3, column=0, padx=10, pady=5)

    def show_admin_menu(self):
        self.clear_buttons()

        self.display_books_button = tk.Button(self.main_menu_frame, text="Display Books", command=self.display_books_window)
        self.display_books_button.grid(row=2, column=0, padx=10, pady=5)

        self.add_book_button = tk.Button(self.main_menu_frame, text="Add Book", command=self.add_book_window)
        self.add_book_button.grid(row=2, column=1, padx=10, pady=5)

        self.delete_book_button = tk.Button(self.main_menu_frame, text="Delete Book", command=self.delete_book_window)
        self.delete_book_button.grid(row=3, column=0, padx=10, pady=5)

        self.add_user_button = tk.Button(self.main_menu_frame, text="Add New User", command=self.add_user_window)
        self.add_user_button.grid(row=3, column=1, padx=10, pady=5)

    def clear_buttons(self):
        for widget in self.main_menu_frame.winfo_children():
            widget.destroy()

        self.student_button = tk.Button(self.main_menu_frame, text="Student", command=self.show_student_menu)
        self.student_button.grid(row=0, column=0, padx=10, pady=5)

        self.admin_button = tk.Button(self.main_menu_frame, text="Admin", command=self.show_admin_menu)
        self.admin_button.grid(row=0, column=1, padx=10, pady=5)

        self.exit_button = tk.Button(self.main_menu_frame, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def display_books_window(self):
        self.display_books_window = tk.Toplevel(self.root)
        self.display_books_window.title("Display Books")

        scrollbar = tk.Scrollbar(self.display_books_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_area = tk.Text(self.display_books_window, yscrollcommand=scrollbar.set)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar.config(command=text_area.yview)

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            cursor.close()
            
            if books:
                for book in books:
                    text_area.insert(tk.END, f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Edition: {book[3]}, Copies: {book[4]}\n")
            else:
                text_area.insert(tk.END, "No books found in the library.")
        except psycopg2.Error as error:
            messagebox.showerror("Error", f"Database error: {error}")

    def add_book_window(self):
        self.add_book_window = tk.Toplevel(self.root)
        self.add_book_window.title("Add Book")
        
        tk.Label(self.add_book_window, text="Enter Book Title: ").grid(row=0, column=0, padx=10, pady=5)
        self.book_title_entry = tk.Entry(self.add_book_window)
        self.book_title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.add_book_window, text="Enter Author: ").grid(row=1, column=0, padx=10, pady=5)
        self.author_entry = tk.Entry(self.add_book_window)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.add_book_window, text="Enter Edition: ").grid(row=2, column=0, padx=10, pady=5)
        self.edition_entry = tk.Entry(self.add_book_window)
        self.edition_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.add_book_window, text="Enter Copies: ").grid(row=3, column=0, padx=10, pady=5)
        self.copies_entry = tk.Entry(self.add_book_window)
        self.copies_entry.grid(row=3, column=1, padx=10, pady=5)
