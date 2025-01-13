# To-Do List Application with Java Swing.
---
## Overview
This project is a **To-Do List Application** implemented using **Java Swing** for the GUI and **MySQL** for the database backend. The application allows users to manage their tasks by adding, deleting, updating, and viewing them. It showcases the integration of a GUI-based application with a relational database.

---

## Features
1. **Add Task**: Allows users to add a new task with the following attributes:
   - Title
   - Description
   - Status (e.g., pending/completed)
   - Due Date

2. **Delete Task**: Enables users to delete an existing task by providing its unique Task ID.

3. **Update Task Status**: Allows users to update the status of a specific task (e.g., from pending to completed).

4. **View All Tasks**: Displays a table containing all tasks stored in the database with attributes such as ID, Title, Description, Status, Due Date, and Created At.

5. **Database Integration**: All operations are performed on a MySQL database, ensuring data persistence.

---

## Technologies Used
- **Programming Language**: Java
- **GUI Framework**: Java Swing
- **Database**: MySQL
- **IDE**: IntelliJ IDEA / Eclipse / Any Java IDE

---

## Database Setup
1. Install MySQL on your system.
2. Create a database named `todo_list`.
3. Create a table named `tasks` with the following structure:
   ```sql
   CREATE TABLE tasks (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       description TEXT,
       status ENUM('pending', 'completed') NOT NULL,
       due_date DATE,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
## Steps to Display..
**step 1)**
![Screenshot (106)](https://github.com/user-attachments/assets/a93abec9-da2c-4b2c-bcbd-165df203ecdd)

**step 2)**
![Screenshot (107)](https://github.com/user-attachments/assets/43693aa5-3a28-4b13-b2d2-76d7e685c6de)

**step 3)**
![Screenshot (108)](https://github.com/user-attachments/assets/887eb12d-de29-458a-a606-94fcd8d8d35b)
![Screenshot (109)](https://github.com/user-attachments/assets/fe726634-75a9-452e-aa4a-5ec6cd8e4800)
**step 4)**
![Screenshot (110)](https://github.com/user-attachments/assets/3ace624e-7943-4461-a977-cfa626636ccf)
![Screenshot (111)](https://github.com/user-attachments/assets/b1a2a3ed-0e7a-44de-b779-35149dbe0e04)
![Screenshot (112)](https://github.com/user-attachments/assets/7d7c3d09-4062-4241-ba17-ce9f2047eb4d)
**step 5)**
![Screenshot (113)](https://github.com/user-attachments/assets/3b6a3dfa-ffe0-4d8d-a708-8c3da7302c7c)
![Screenshot (114)](https://github.com/user-attachments/assets/f5d01ea5-2314-4ee8-92d1-039dcd596c47)



