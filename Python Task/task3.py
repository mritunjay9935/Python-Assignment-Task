import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mishra@12345",
  database="mystudents"
)

#STEP 1- Create Table 

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (student_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), age INT, grade FLOAT)")

# Inserting the values

sql = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
val = ("Alice", "Smith", 18, 95.5)
mycursor.execute(sql, val)
mydb.commit()

# Updating The value 

sql = "UPDATE students SET grade = 97.0 WHERE first_name = 'Alice'"
mycursor.execute(sql)
mydb.commit()

# Deleting the record

sql = "DELETE FROM students WHERE last_name = 'Smith'"
mycursor.execute(sql)
mydb.commit()

# Now, Fetch and display all the records

mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


