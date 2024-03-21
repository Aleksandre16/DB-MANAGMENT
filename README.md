# Student-Advisor Database Management 

This Python script manages a SQLite database for tracking student-advisor relationships. It allows users to create, populate, and query a database containing information about students and their advisors.

## Setup

1. **Installation:**
   - Ensure you have Python installed on your system.
   - Install the required packages by running:
     ```
     pip install -r requirements.txt
     ```
     DONT NEED ANY REQUIREMENTS FOR NOW!

2. **Database Initialization:**
   - The script initializes a SQLite database named `sqlite3.db`.
   - It creates three tables: `Advisor`, `Student`, and `StudentAdvisor`.
   - The `Advisor` table stores information about advisors.
   - The `Student` table stores information about students.
   - The `StudentAdvisor` table establishes the many-to-many relationship between students and advisors.

## Usage

1. **Populating the Database:**
   - Modify the script to add or update data as per your requirements.
   - Run the script to populate the database with the desired information.

2. **Querying the Database:**
   - Use the provided SQL queries to retrieve information from the database.
   - Modify the queries as needed to extract specific data.

3. **Viewing Results:**
   - Execute the script to see the list of advisors with the number of their students.


