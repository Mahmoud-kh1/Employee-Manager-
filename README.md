# Employee Management System (Tkinter + SQLite)

A small desktop app to manage employees — add, update, delete, and browse employee records in a simple GUI built with `tkinter` and stored in an `SQLite` database.  
Designed to be minimal, readable, and easy to run locally.

---

![App Screenshot](https://github.com/Mahmoud-kh1/Employee-Manager-/blob/main/images/Screenshot%202025-09-07%20131223.png?raw=true)

##  About
This project is a lightweight Employee Management System written in Python using:
- `tkinter` for the GUI
- `sqlite3` for persistent storage (single-file `Employee.db`)

---

##  Features
-  Add new employees (name, age, job, email, gender, mobile, address)  
-  Select a row to populate the form for editing  
-  Update selected employee  
-  Delete selected employee (with confirmation)  
-  Clear form  
-  Treeview listing of all employees  
-  Safe DB creation and automatic seeding of sample data (first run only)  
-  Minimal defensive checks and error messages  

---

##  Requirements
- **Python 3.8+** (3.10 / 3.11 recommended)  
- Standard library only — **no external pip packages required**:
  - `tkinter` (usually included with standard Python builds)  
  - `sqlite3` (part of Python stdlib)  


