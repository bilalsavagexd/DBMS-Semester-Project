# Functions:

# Add Book Function
def addbook():
bn = input("Enter BOOK Name : ")
c = input("Enter BOOK Code: ")
t = input("Total Books : ")
s = input("Enter Subject: ")
data = (bn,c,t,s)
sql = 'insert into books values(%s,%s,%s,%s)*
c = con.cursor()
c.execute(sql,data)
con.commit()
print(">--------------------------------------------------<")
print("Data Entered Successfully")

# Issue Book Function
def issuebook():
n = input("Enter Name : ")
r = input("Enter Reg No : ")
co = input("Enter Book Code : ")
d = input("Enter Date : "|I
a = "insert into issue values(%s,%s,%s,%s)"
data = (n,r,co,d)
c = con.cursor()
c.execute(a,data)
con.commit()
print（">-------------------------------------------------<")
print("Book issued to : ",n)
bookup(co,-1)


# Submit Book Function
def submitbook():
n = input("Enter Name : ")
r = input("Enter Reg No: ")
co = input("Enter Book Code : ")
d = input("Enter Date: "
a = "insert into submit values(%s,%s,%s,%s)"
data = (n,r,co,d)
c = con.cursor)
c.execute(a,data)
con.commit()
print(">-------------------------------------------------<")
print("Book Submitted from : ",n)
bookup(co, 1)