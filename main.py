from tkinter import *
from tkinter import ttk 

root = Tk()
root.title('Employee Managment System')
root.geometry('1250x615+0+0')
root.resizable(False, False)
root.configure(bg = '#2c3e50')

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
txtName = Entry(entry_frame, width= 20, font = ('Calibri', 16, 'bold'))
txtName.place(x = 120, y = 50)


LblJob = Label(entry_frame, text = "Job", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblJob.place(x = 10, y = 90)
txtJob = Entry(entry_frame, width= 20, font = ('Calibri', 16, 'bold'))
txtJob.place(x = 120, y = 90) 

LblGender = Label(entry_frame, text = "Gender", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblGender.place(x = 10, y = 130)
comboGender = ttk.Combobox(entry_frame,state= 'readonly', width= 18,font = ('Calibri', 16, 'bold')  )
comboGender['values'] = ("Male", "Female")
comboGender.place(x = 120, y =130)


LblAge = Label(entry_frame, text = "Age", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblAge.place(x = 10, y = 170)
txtAge= Entry(entry_frame, width= 20, font = ('Calibri', 16, 'bold'))
txtAge.place(x = 120, y = 170) 


LblEmail = Label(entry_frame, text = "Email", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblEmail.place(x = 10, y = 210)
txtEmail= Entry(entry_frame, width= 20, font = ('Calibri', 16, 'bold'))
txtEmail.place(x = 120, y = 210) 


LblMob = Label(entry_frame, text = "Moblie", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblMob.place(x = 10, y = 250)
txtMob= Entry(entry_frame, width= 20, font = ('Calibri', 16, 'bold'))
txtMob.place(x = 120, y = 250) 


LblAdderss = Label(entry_frame, text = "Address :", font = ('Calibri', 16, 'bold'), bg = '#2c3e50', fg= 'white' )
LblAdderss.place(x = 10, y = 290)
txtAddress = Text(entry_frame, width= 30, height= 2 ,font = ('Calibri', 16, 'bold') )
txtAddress.place(x = 10, y = 330)


#===========[Define] ======= 
def hide():
    root.geometry("375x525")

def show(): 
   root.geometry('1250x615+0+0')


btnHide = Button(entry_frame, text = 'HIDE',bg ='white', bd = 1, relief= SOLID,cursor='hand2', command= hide)
btnHide.place(x = 270, y = 10)


btnShow = Button(entry_frame, text = 'SHOW',bg ='white', bd = 1, relief= SOLID, cursor='hand2', command= show)
btnShow.place(x = 310, y = 10)

#===== Buttons ===== #
btnFrame = Frame(entry_frame, bg = '#2c3e50', bd = 1, relief= SOLID)
btnFrame.place(x = 10, y = 400, width= 335, height= 100)

btnAdd = Button(btnFrame,
                text = "Add Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#16a085', bd = 0
                ).place(x = 4, y = 5)

btnEdit = Button(btnFrame,
                text = "Update Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#2980b9', bd = 0
                ).place(x = 4, y = 50)


btnEdit = Button(btnFrame,
                text = "Delete Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#c0392b', bd = 0
                ).place(x = 170, y = 5)


btnClear = Button(btnFrame,
                text = "Clear Details",
                width = 14,
                height= 1,
                font = ('Calibri'),
                fg = 'white',
                bg = '#f39c12', bd = 0
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

tv.place(x = 1, y = 1, height= 610, width=875)


root.mainloop()  

