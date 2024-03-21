import sqlite3
# Change Dialect to avoid any warnings.
# Connect to SQLite database
# New file created if it doesn't already exist
conn = sqlite3.connect('sqlite3.db')

# Create cursor object
cursor = conn.cursor()

# Create and populate tables
cursor.executescript(''' 
CREATE TABLE IF NOT EXISTS Advisor( 
    AdvisorID INTEGER PRIMARY KEY, 
    AdvisorName TEXT NOT NULL
); 

CREATE TABLE IF NOT EXISTS Student( 
    StudentID INTEGER PRIMARY KEY, 
    StudentName TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS StudentAdvisor(
    StudentID INTEGER,
    AdvisorID INTEGER,
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
    PRIMARY KEY(StudentID, AdvisorID)
); 

INSERT OR IGNORE INTO Advisor(AdvisorID, AdvisorName) VALUES 
(1,"John Paul"), 
(2,"Anthony Roy"), 
(3,"Raj Shetty"), 
(4,"Sam Reeds"), 
(5,"Arthur Clintwood"); 

INSERT OR IGNORE INTO Student(StudentID, StudentName) VALUES 
(501,"Geek1"), 
(502,"Geek2"), 
(503,"Geek3"), 
(504,"Geek4"), 
(505,"Geek5"), 
(506,"Geek6"), 
(507,"Geek7"), 
(508,"Geek8"), 
(509,"Geek9"), 
(510,"Geek10"); 

INSERT OR IGNORE INTO StudentAdvisor(StudentID, AdvisorID) VALUES 
(501, 1),
(502, 1),
(503, 3),
(504, 2),
(505, 4),
(506, 2),
(507, 2),
(508, 3),
(509, 1),
(509, 2),
(510, 1); 
''')

# Commit changes to database
conn.commit()

# TO demonstrate students having multiple advisors!
cursor.execute('''
INSERT OR IGNORE INTO StudentAdvisor(StudentID, AdvisorID) VALUES 
(501, 1),
(501, 3);  -- Student 501 with Advisor 1 and Advisor 3, in db "StudentAdvisor".
''')

# Commit changes to database
conn.commit()

cursor.execute('''
SELECT Advisor.AdvisorID, Advisor.AdvisorName, COUNT(Student.StudentID) AS NumStudents
FROM Advisor
LEFT JOIN StudentAdvisor ON Advisor.AdvisorID = StudentAdvisor.AdvisorID
LEFT JOIN Student ON StudentAdvisor.StudentID = Student.StudentID
GROUP BY Advisor.AdvisorID, Advisor.AdvisorName
ORDER BY Advisor.AdvisorID
''')

advisors_with_students = cursor.fetchall()

# Print the list of advisors with the number of their students
for advisor in advisors_with_students:
    print(f"Advisor {advisor[0]} ({advisor[1]}) has {advisor[2]} students.")
print("Check DB for all students.")
# Closing the connection
conn.close()
