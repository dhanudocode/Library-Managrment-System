'''import mysql.connector

a=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
b=a.cursor()

b.execute("CREATE DATABASE LIBRARY")'''


'''import mysql.connector
a=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LIBRARY"
)
b=a.cursor()
b.execute("""
    CREATE TABLE LOG_IN(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20),
    Username VARCHAR(50),
    Password VARCHAR(50)
    )
""")
print("Table created")'''

'''import mysql.connector
a=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)
b=a.cursor()
c="INSERT INTO log_in(NAME, USERNAME, PASSWORD) VALUES (%s,%s,%s)"
d=[
    ("Alan walker","alan35","34565"),
    ("Taylor swift","taylor09","43263"),
    ("Johnny huynh","johnny38","93260"),
    ("Selena gomez","selena94","78253"),
    ("yung kai","kai48","57458"),
    ("Ed Sheeran","ed77","12894"),
    ("Justin Bieber","justin45","90321"),
    ("Dua Lipa","dualipa56","23489"),
    ("Charlie Puth","charlie27","96421"),
    ("Sia","sia11","49273")
    ]
b.executemany(c,d)
a.commit()
print("rows created")'''



'''import mysql.connector
a=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LIBRARY"
)
b=a.cursor()
b.execute("""
    CREATE TABLE BOOKS(
    BOOK_ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR (50),
    STATUS VARCHAR (20)
    )
""")
print("Table created")import mysql.connector
a=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LIBRARY"
)
b=a.cursor()
b.execute("""
    CREATE TABLE BOOKS(
    BOOK_ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR (50),
    STATUS VARCHAR (20),
    Booked_by
    )
""")
print("Table created")'''



'''import mysql.connector
a=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)
b=a.cursor()
c="INSERT INTO Books(TITLE, AUTHOR, GENRE, STATUS) VALUES (%s,%s,%s,%s)"
d=[
    ("Dune","Frank Herbert","Science Fiction / Space","available"),
    ("Braiding Sweetgrass","R.W.Kimmerer","Non-Fiction / Nature","Availabl"),
    ("The Immortals of Meluha","A.Tripathi","Fantasy","Booked"),
    ("Tinkle Digest/Double Digest","Multiple Writers","Comics & Graphic","Booked"),
    ("The Art of Travel"," A.D.Botton","Travel Essay","Booked")
    ("Dracula", "Bram Stoker", "Horror", "available"),
    ("The Bourne Identity", "Robert Ludlum", "Action / Thriller", "booked"),
    ("Civil War", "Mark Millar", "Marvel Comics", "Available"),
    ("TinyTAN Story Universe", "HYBE", "Fantasy / BTS", "Booked"),
    ("Treasure Island", "Robert Louis Stevenson", "Adventure", "Available"),
    ("The Hound of the Baskervilles", "Arthur Conan Doyle", "Mystery", "Available"),
    ("The Time Machine", "H.G. Wells", "Time Travel / Science Fiction", "Available"),
    ("Atomic Habits", "James Clear", "Self-Improvement", "Available"),
    ("Think and Grow Rich", "Napoleon Hill", "Success", "Booked"),
    ("Gray's Anatomy", "Henry Gray", "Medicine", "Available"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell & Peter Norvig", "Artificial Intelligence", "Available")
    ]
b.executemany(c,d)
a.commit()
print("rows created")'''



from tkinter import *
from tkinter import messagebox
import mysql.connector


try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="LIBRARY"
    )
    
    cur = con.cursor(buffered=True)
    
except Exception as e:
    messagebox.showerror("Connection Error", f"Failed to connect to Database: {e}")


def open_thank_you_page():
    thank = Toplevel()
    thank.title("Booking Successful")
    thank.geometry("500x300")
    thank.configure(bg="Light blue")

    Label(thank, text="THANK YOU!", font=("Arial", 24, "bold"),
          bg="pink", fg="green").pack(pady=30)
    Label(thank, text="Your book has been successfully booked.",
          font=("Arial", 12), bg="yellow", fg="black").pack(pady=10)
    Label(thank, text="Please collect it from the library counter.",
          font=("Arial", 12), bg="yellow", fg="black").pack()

    Button(thank, text="Exit", font=("Arial", 12),
           bg="black", fg="white", command=root.destroy).pack(pady=30)


def open_book_details(book_data, dashboard_window):
    b_id, b_title, b_author, b_genre, b_status, b_prev_user, b_days = book_data

    details = Toplevel()
    details.title("Book Details")
    details.geometry("500x450")
    details.configure(bg="light blue")

    Label(details, text="BOOK DETAILS", font=("Arial", 18, "bold"),
          bg="black", fg="white").pack(pady=20)

    Label(details, text=f"Title: {b_title}", font=("Arial", 14, "bold"),
          bg="gray", fg="white").pack(anchor="w", padx=30, pady=5)
    Label(details, text=f"Author: {b_author}", font=("Arial", 12),
          bg="pink", fg="black").pack(anchor="w", padx=30, pady=2)
    Label(details, text=f"Concept/Genre: {b_genre}", font=("Arial", 12),
          bg="pink", fg="black").pack(anchor="w", padx=30, pady=2)
    

    if b_status.lower() == "available":
        Label(details, text=f"Current Status: {b_status.upper()}",
              font=("Arial", 12, "bold"), bg="white", fg="green").pack(anchor="w", padx=30, pady=5)
    else:
        Label(details, text=f"Current Status: {b_status.upper()}",
              font=("Arial", 12, "bold"), bg="white", fg="red").pack(anchor="w", padx=30, pady=5)

    Label(details, text=f"Previously Used By: {b_prev_user}",
          font=("Arial", 11), bg="pink", fg="black").pack(anchor="w", padx=30, pady=2)

    if b_status.lower() == "booked":
        Label(details, text=f"Booked For: {b_days} days",
              font=("Arial", 11), bg="white", fg="red").pack(anchor="w", padx=30, pady=2)

    def confirm_booking():
        try:
            cur.execute("UPDATE BOOKS SET STATUS='Booked', BOOKED_DAYS=7 WHERE BOOK_ID=%s", (b_id,))
            con.commit()
            details.destroy()
            dashboard_window.destroy()
            open_thank_you_page()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to book: {e}")

    if b_status.lower() == "available":
        Button(details, text="CONFIRM BOOKING", font=("Arial", 12),
               bg="green", fg="white", command=confirm_booking).pack(pady=30)
    else:
        Label(details, text="This book cannot be booked right now.",
              font=("Arial", 11), bg="red", fg="white").pack(pady=30)


def open_dashboard():
    root.withdraw()

    dashboard = Toplevel()
    dashboard.title("Library Inventory Dashboard")
    dashboard.geometry("750x450")
    dashboard.configure(bg="light blue")

    Label(dashboard, text="LIBRARY INVENTORY", font=("Arial", 18, "bold"),
          bg="black", fg="white").pack(pady=20)

    table_frame = Frame(dashboard, bg="pink")
    table_frame.pack(fill="both", expand=True, padx=30, pady=(0, 10))

    scrollbar = Scrollbar(table_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    from tkinter import ttk
    cols = ("ID", "Title", "Author", "Concept","Status")
    book_table = ttk.Treeview(table_frame, columns=cols, show="headings",
                               yscrollcommand=scrollbar.set)
    scrollbar.config(command=book_table.yview)
    

    widths = {"ID": 60, "Title": 250, "Author": 180, "Concept": 180, "Status": 100}
    for col in cols:
        book_table.heading(col, text=col.upper(), anchor="w")
        book_table.column(col, width=widths[col])
    book_table.pack(fill="both", expand=True)

    book_data_store = {}

    try:
        cur.execute("SELECT * FROM BOOKS")
        for row in cur.fetchall():
            padded_row = list(row)
            book_data_store[str(padded_row[0])] = padded_row
            book_table.insert("", "end", values=(padded_row[0], padded_row[1],
                                                  padded_row[2], padded_row[3],padded_row[4]))
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not fetch books: {e}")

    def view_selected_book():
        selected = book_table.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a book first.")
            return
        values = book_table.item(selected, "values")
        book_id = str(values[0])
        full_book_data = book_data_store[book_id]
        open_book_details(full_book_data, dashboard)

    Button(dashboard, text="VIEW DETAILS", font=("Arial", 12),
           bg="black", fg="white", command=view_selected_book).pack(pady=20)

    dashboard.protocol("WM_DELETE_WINDOW", root.destroy)


def login():
    
    username = user_entry.get()
    password = pass_entry.get()
    
    sql = "SELECT * FROM login WHERE username=%s AND password=%s"
    
    cur.execute(sql, (username, password))
    
    result = cur.fetchone()
    
    if result:
        messagebox.showinfo("Success", "Login Successful")
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

root = Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="light blue")

Label(root, text="LOGIN PAGE", font=("Arial", 18, "bold"),
      bg="black", fg="white").pack(pady=20)
Label(root, text="Username", font=("Arial", 12),
      bg="gray", fg="white").pack()
user_entry = Entry(root, width=30)
user_entry.pack(pady=5)
user_entry.focus()

Label(root, text="Password", font=("Arial", 12),
      bg="gray", fg="white").pack()
pass_entry = Entry(root, show="*", width=30)
pass_entry.pack(pady=5)

Button(root, text="Login", font=("Arial", 12),
       bg="black", fg="white", command=login).pack(pady=20)

root.mainloop()
