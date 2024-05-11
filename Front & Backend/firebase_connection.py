import psycopg2
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate(r"C:\Users\Hp\OneDrive\Desktop\DBMS-Semester-Project\Library_Management_System\serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://dbms--semester-project-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Establish connection to SQL database
db_connection = psycopg2.connect(
    host="localhost",
    database="Library_Management_System",
    user="postgres",
    password="2354232"
)

# Function to sync data from SQL database to Firebase Realtime Database
def sync_data():
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        # Convert SQL data to Firebase format and update Firebase database
        firebase_ref = db.reference('books')
        for book in books:
            firebase_ref.child(str(book[0])).set({
                'title': book[1],
                'author': book[2],
                'edition': book[3],
                'copies': book[4]
            })

    except psycopg2.Error as error:
        print("Error syncing data:", error)

# Function to listen for real-time updates from Firebase Realtime Database
def listen_for_updates():
    firebase_ref = db.reference('books')
    firebase_ref.listen(lambda event: print(event.event_type, event.data))

# Call synchronization function
sync_data()

# Call function to listen for real-time updates
listen_for_updates()
