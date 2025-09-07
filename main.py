from tkinter import *
from tkinter import ttk 
from db import Database
from tkinter import messagebox
import os

# Debug: show which DB file is being opened (helps catch "different working dir" issue)
print("Using DB file:", os.path.abspath("Employee.db"))

db = Database("Employee.db")

# --- seed initial data if the table is empty (runs once on first start)
def seed_initial_data():
    try:
        existing = db.fetch()
    except Exception:
        existing = []
    if not existing:
        sample = [
            ('Ahmed Hassan','29','Software Engineer','ahmed.hassan@example.com','Male','01011223344','123 Nile St, Cairo'),
            ('Sara Mahmoud','26','HR Specialist','sara.mahmoud@example.com','Female','01022334455','45 Tahrir Sq, Cairo'),
            ('Mahmoud Khaled','32','Project Manager','mahmoud.k@example.com','Male','01033445566','12 Corniche Rd, Alexandria'),
            ('Fatma Ali','24','UX Designer','fatma.ali@example.com','Female','01044556677','8 Zamalek Island, Cairo'),
            ('Youssef Ramadan','35','Accountant','youssef.r@example.com','Male','01055667788','77 Heliopolis, Cairo'),
            ('Lina Samir','28','Marketing Exec','lina.samir@example.com','Female','01066778899','5 Nasr City, Cairo'),
            ('Omar Farouk','30','DevOps Engineer','omar.farouk@example.com','Male','01077889900','9 Maadi, Cairo'),
            ('Dalia Naguib','27','Business Analyst','dalia.naguib@example.com','Female','01088990011','101 Raml Station, Alexandria'),
            ('Karim Adel','31','QA Engineer','karim.adel@example.com','Male','01099001122','22 Dokki, Giza'),
            ('Mona Youssef','29','Sales Manager','mona.y@example.com','Female','01010101010','3 Garden City, Cairo'),
            ('Tamer Saleh','33','Network Admin','tamer.saleh@example.com','Male','01012121212','14 New Cairo'),
            ('Nora Ibrahim','25','Content Writer','nora.ibrahim@example.com','Female','01013131313','56 Sphinx Rd, Giza')
        ]
        for s in sample:
            try:
                db.insert(*s)
            except Exception:
                # ignore individual insert failures during seeding
                pass

# call seeder
seed_initial_data()

root = Tk()
root.title('Employee Managment System')
root.geometry('1250x615+0+0')
root.resizable(False, False)
root.configure(bg = '#2c3e50')


name  = StringVar()
age  = StringVar()
job  = StringVar()
gender  = StringVar()
email  = StringVar()
mobile  = StringVar()


logo = PhotoImage(file='lgo.png')

lblLogo = Label(root, image = logo)
lblLogo.place(x = 80, y = 520)




#======= Entity Frame ======#
entry_frame = Frame(root, bg ='#2c3e50')
entry_frame.place(x = 1, y = 1, width= 360, height=510)
title = Label(entry_frame, text = 'Employee Company', font = ('Calibri', 18, 'bold'), bg = '#2c3e50', fg= 'white')
title.place(x = 10, y = 1)


LblName = Label(entry_frame, text = "Name", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblName.place(x = 10, y = 50)
txtName = Entry(entry_frame,textvariable =name, width= 20, font = ('Calibri', 16, 'bold'))
txtName.place(x = 120, y = 50)


LblJob = Label(entry_frame, text = "Job", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblJob.place(x = 10, y = 90)
txtJob = Entry(entry_frame,textvariable =job, width= 20, font = ('Calibri', 16, 'bold'))
txtJob.place(x = 120, y = 90) 

LblGender = Label(entry_frame, text = "Gender", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblGender.place(x = 10, y = 130)
comboGender = ttk.Combobox(entry_frame,textvariable =gender,state= 'readonly', width= 18,font = ('Calibri', 16, 'bold')  )
comboGender['values'] = ("Male", "Female")
comboGender.place(x = 120, y =130)


LblAge = Label(entry_frame, text = "Age", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblAge.place(x = 10, y = 170)
txtAge= Entry(entry_frame,textvariable = age, width= 20, font = ('Calibri', 16, 'bold'))
txtAge.place(x = 120, y = 170) 


LblEmail = Label(entry_frame, text = "Email", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblEmail.place(x = 10, y = 210)
txtEmail= Entry(entry_frame,textvariable =email, width= 20, font = ('Calibri', 16, 'bold'))
txtEmail.place(x = 120, y = 210) 


LblMob = Label(entry_frame, text = "Moblie", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblMob.place(x = 10, y = 250)
txtMob= Entry(entry_frame, textvariable=mobile, width= 20, font = ('Calibri', 16, 'bold'))
txtMob.place(x = 120, y = 250) 


LblAdderss = Label(entry_frame, text = "Address :", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblAdderss.place(x = 10, y = 290)
txtAddress = Text(entry_frame, width= 30, height= 2 ,font = ('Calibri', 16, 'bold') )
txtAddress.place(x = 10, y = 330)


# keep track of currently selected row (tuple from DB)
row = None

#===========[Define] ======= 
def hide():
    root.geometry("375x525")

def show(): 
   root.geometry('1250x615+0+0')


btnHide = Button(entry_frame, text = 'HIDE',bg ='white', bd = 1, relief= SOLID,cursor='hand2', command= hide)
btnHide.place(x = 270, y = 10)


btnShow = Button(entry_frame, text = 'SHOW',bg ='white', bd = 1, relief= SOLID, cursor='hand2', command= show)
btnShow.place(x = 310, y = 10)




def getData(event):
    global row
    selectedRow = tv.focus()
    if not selectedRow:
        return
    data = tv.item(selectedRow)
    vals = data.get("values", [])
    if not vals:
        return
    row = vals
    # defensive: ensure the tuple has expected length
    try:
        name.set(row[1])
        age.set(row[2])
        job.set(row[3])
        email.set(row[4])
        gender.set(row[5])
        mobile.set(row[6])
        txtAddress.delete(1.0, END)
        txtAddress.insert(END, row[7])
    except Exception:
        # if something unexpected happens, clear selection
        row = None

# --- accept optional event so it can be called directly or as handler
def displayAll(event=None):
    tv.delete(*tv.get_children())
    for r in db.fetch():
        tv.insert("", END, values=r)


def clear_fields():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    mobile.set("")
    txtAddress.delete(1.0, END)


def addEmployess():
    # use .strip() for text widget check so pure newline doesn't bypass the check
    if (txtName.get().strip() == "" or txtAge.get().strip() == "" or txtJob.get().strip() == "" or txtEmail.get().strip() == "" or comboGender.get().strip() == "" or txtMob.get().strip() == "" or txtAddress.get(1.0, END).strip() == ""):
        messagebox.showerror("Error", "please fill all fields")
        return 

    address = txtAddress.get(1.0, END).strip()

    # insert into DB (unchanged)
    db.insert(
        txtName.get().strip(),
        txtAge.get().strip(),
        txtJob.get().strip(),
        txtEmail.get().strip(), 
        comboGender.get().strip(),
        txtMob.get().strip(),
        address
        )  

    messagebox.showinfo("Success", "Added new employee")

    # refresh the Treeview so new row appears
    displayAll()

    # clear fields after add
    clear_fields()


def updateEmployess():
    global row
    if not row:
        messagebox.showwarning("Warning", "Please select a record to update")
        return

    try:
        emp_id = row[0]
    except Exception:
        messagebox.showerror("Error", "Invalid selection")
        return

    if (txtName.get().strip() == "" or txtAge.get().strip() == "" or txtJob.get().strip() == "" or txtEmail.get().strip() == "" or comboGender.get().strip() == "" or txtMob.get().strip() == "" or txtAddress.get(1.0, END).strip() == ""):
        messagebox.showerror("Error", "please fill all fields")
        return

    address = txtAddress.get(1.0, END).strip()

    db.update(emp_id,
              txtName.get().strip(),
              txtAge.get().strip(),
              txtJob.get().strip(),
              txtEmail.get().strip(),
              comboGender.get().strip(),
              txtMob.get().strip(),
              address)

    messagebox.showinfo("Success", "Employee updated")
    displayAll()
    clear_fields()
    row = None


def deleteEmployess():
    global row
    if not row:
        messagebox.showwarning("Warning", "Please select a record to delete")
        return

    try:
        emp_id = row[0]
    except Exception:
        messagebox.showerror("Error", "Invalid selection")
        return

    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?"):
        db.remove(emp_id)
        messagebox.showinfo("Success", "Employee deleted")
        displayAll()
        clear_fields()
        row = None


#===== Buttons ===== #
btnFrame = Frame(entry_frame, bg = '#2c3e50', bd = 1, relief= SOLID)
btnFrame.place(x = 10, y = 400, width= 335, height= 100)

Button(btnFrame,
                text = "Add Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#16a085', bd = 0, 
                command= addEmployess
                ).place(x = 4, y = 5)

Button(btnFrame,
                text = "Update Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#2980b9', bd = 0,
                command= updateEmployess
                ).place(x = 4, y = 50)


Button(btnFrame,
                text = "Delete Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#c0392b', bd = 0,
                command= deleteEmployess
                ).place(x = 170, y = 5)


Button(btnFrame,
                text = "Clear Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#f39c12', bd = 0,
                command= clear_fields
                ).place(x = 170, y = 50)  



#========== Table Frame ============# 
treeFrame = Frame(root , bg = 'white')
treeFrame.place(x = 365, y = 1, width= 875, height=610)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 13),rowheight = 50)
style.configure("mystyleTreeview", font = ('Calibri', 13))

tv = ttk.Treeview(treeFrame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text= "ID")
tv.column("1", width="40") 

tv.heading("2", text= "Name")
tv.column("2", width="140") 

tv.heading("3", text= "Age")
tv.column("3", width="50") 


tv.heading("4", text= "Job")
tv.column("4", width="120") 


tv.heading("5", text= "Email")
tv.column("5", width="150") 

tv.heading("6", text= "Gender")
tv.column("6", width="90") 


tv.heading("7", text= "Mobile")
tv.column("7", width="150") 


tv.heading("8", text= "Address")
tv.column("8", width="150") 

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.place(x = 1, y = 1, height= 610, width=875)
 
displayAll()
root.mainloop()
