from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import time
import datetime
from tkinter import messagebox

#OPENING 
root = Tk()
root.title("UFIX LTD Payroll system")
width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg = "#81F7F3")

#VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
emp_name = StringVar()
emp_addr = StringVar()
emp_ni = StringVar()
SEARCH = StringVar()
NAME = StringVar() 
Ninumber = StringVar() 
hoursworked = StringVar() 
hourlyrate = StringVar() 
tax = StringVar() 
overtime = StringVar() 
netpay = StringVar()
dateoforder = StringVar()
payable = StringVar()
Name = StringVar()
Address = StringVar()
HoursWorked = StringVar()
WagesHour = StringVar()
Payable = StringVar()
Taxable = StringVar()
NetPayable = StringVar()
Employer = StringVar()
NINumber = StringVar()
DateOfOrder = StringVar()
privacyString = StringVar()
DateOfOrder.set(time.strftime("%d/%m/%Y"))

global loginformOptions
global admin_id
global viewform
global tree  
#destroy file to opinion
def DestroyFileToOption():
    root.withdraw()
    LoginForm()

#button options to login
def LoginForm():

    global loginformOptions
    loginformOptions = Toplevel()
    loginformOptions.title("Login")
    width = 1024
    height = 739
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginformOptions.resizable(0, 0)
    loginformOptions.geometry("%dx%d+%d+%d" % (width, height, x, y))
    loginformOptions.configure( bg = "#81F7F3")

    #FRAME
    Title = Frame(loginformOptions, bd=1, relief=FLAT)
    Title.pack()

    #top frame for titles
    TopLoginFormOptions = Frame(loginformOptions, width=600, height=100, bd=1, relief=FLAT, bg = "#81F7F3")
    TopLoginFormOptions.pack(side=TOP, pady=20)

    #login title
    lbl_text = Label(TopLoginFormOptions, text="Login", font=('arial', 45), bg = "white")
    lbl_text.pack(fill=X)

    #middle frame for buttons
    MidLoginFormOptions = Frame(loginformOptions, width=600, bg = "#81F7F3")
    MidLoginFormOptions.pack(side=TOP, pady=50)

    #login button
    btn_login = Button(MidLoginFormOptions, text="Associate Login", font=('arial', 18), width=30, bg="#01A9DB", command=DestroyOptionToAssocLog)
    btn_login.grid(row=2, columnspan=2, pady=20)

    #login button
    btn_adminLogin = Button(MidLoginFormOptions, text="Admin Login", font=('arial', 18), width=30, bg="#01A9DB", command=DestroyOptionToAdminLog)
    btn_adminLogin.grid(row=3, columnspan=2, pady=20)

    #astetics=======================================================
    #panel 
    Label(loginformOptions, text="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=50).place(x=0, y=0)

    #logo
    lab = Label(TopLoginFormOptions, image=my_logo_pic, bg="#81F7F3").pack()

#------------------------------------------------------------------------------
#login option for associate
def AssociateLogin():

    global lbl_result
    AssociateLoginform = Toplevel()
    AssociateLoginform.title("Associate Login")
    width = 1024
    height = 739
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    AssociateLoginform.resizable(0, 0)
    AssociateLoginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    AssociateLoginform.configure( bg = "#81F7F3")
    TopLoginFormAssoc = Frame(AssociateLoginform, width=600, height=100, bd=1, relief=FLAT, bg = "#81F7F3")
    TopLoginFormAssoc.pack(side=TOP, pady=30)
    #login title
    lbl_text = Label(TopLoginFormAssoc, text="Associate Login", font=('arial', 45), bg = "white")
    lbl_text.pack(fill=X)

    MidLoginFormAssoc = Frame(AssociateLoginform, width=600, bg = "#81F7F3")
    MidLoginFormAssoc.pack(side=TOP, pady=50)
    #username label
    lbl_usernameAssoc = Label(MidLoginFormAssoc, text="Username:", font=('arial', 25), bd=18, bg = "#81F7F3", relief = FLAT)
    lbl_usernameAssoc.grid(row=0)
    #password label
    lbl_passwordAssoc = Label(MidLoginFormAssoc, text="Password:", font=('arial', 25), bd=18, bg = "#81F7F3", relief = FLAT)
    lbl_passwordAssoc.grid(row=1)
    #error label
    lbl_result = Label(MidLoginFormAssoc, text="", font=('arial', 18), bg = "#81F7F3", relief = FLAT)
    lbl_result.grid(row=3, columnspan=2)
    #username text input
    username = Entry(MidLoginFormAssoc, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    #password text input
    password = Entry(MidLoginFormAssoc, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    #login button
    btn_login = Button(MidLoginFormAssoc, text="Login", font=('arial', 18), width=30, bg="#01A9DB", command=AssocLogin)
    btn_login.grid(row=2, columnspan=2, pady=20)
    #back button
    btn_back = Button(MidLoginFormAssoc, text="Back", font=('arial', 18), width=30, bg="#01A9DB", command=BackButton)
    btn_back.grid(row=3, columnspan=2, pady=10)
    #privacy policy
    lbl_privacy = Button(MidLoginFormAssoc, text="By Logging in, you accept our Privacy Policy, click for more information",font=('arial', 14), bg = "#81F7F3", relief = FLAT, command=PrivacyPolicy)
    lbl_privacy.grid(row=4, columnspan=2)
    #astetics=======================================================
    #panel
    Label(AssociateLoginform, text ="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=60).place(x=0,y=0)
    #logo    
    lab = Label(TopLoginFormAssoc, image = my_logo_pic, bg="#81F7F3", relief = FLAT).pack()
   
def AssocDatabase():
    global conn, cursor
    conn = sqlite3.connect("plswork.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `associate` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `associate` WHERE `username` = 'associate' AND `password` = 'associate'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `associate` (username, password) VALUES('associate', 'associate')")
        conn.commit()

def AssocLogin(event=None):

    global admin_id
    AssocDatabase()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `associate` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `associate` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            AssocMainHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()  
    
def DestroyOptionToAssocLog():
    loginformOptions.withdraw()
    AssociateLogin()

def AssocMainHome():

    global Home
    Home = Toplevel()
    Home.title("Associate Home")
    width = 1024
    height = 739
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=FLAT)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Associate Home", font=('arial', 45), bg = "white")
    lbl_display.pack()

#astetics=======================================================
#panel
    Label(Home, text="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=60).place(x=0, y=0)   

#logo
    lab = Label(Home, image=my_logo_pic, bg="#81F7F3").pack()
#astetics=======================================================

#menu options
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit)
    filemenu2.add_command(label="View Payslip", command=DestroyHomePayslip)
    filemenu2.add_command(label="Time Off Requests", command=TOReq)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Options", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#81F7F3")

def PrivacyPolicy():

    global Loginform
    Loginform = Toplevel()
    Loginform.title("Privacy Policy")
    width = 1024
    height = 739
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    Loginform.resizable(0, 0)
    Loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Loginform.configure( bg = "#81F7F3")
    TopLoginFormAssoc = Frame(Loginform, width=600, height=100, bd=1, relief=FLAT, bg = "#81F7F3")
    TopLoginFormAssoc.pack(side=TOP, pady=10)
    #login title
    lbl_text = Label(TopLoginFormAssoc, text="Privacy Policy", font=('arial', 45), bg = "white")
    lbl_text.pack(fill=X)

    MidLoginFormAssoc = Frame(Loginform, width=600, bg = "#81F7F3")
    MidLoginFormAssoc.pack(side=TOP)

    

    lbl_policy = Label(MidLoginFormAssoc, textvariable = privacyString, bg = "#81F7F3", anchor = "w")
    lbl_policy.grid(row=0, columnspan=2, pady=10)

    #back button
    btn_back = Button(MidLoginFormAssoc, text="Back", font=('arial', 18), width=30, bg="#01A9DB", command=BackButtonPrivacy)
    btn_back.grid(row=1, columnspan=2, pady=10)

    #astetics=======================================================
    #panel
    Label(Loginform, text ="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=60).place(x=0,y=0)

    privacyString.set("The type of personal information we collect. We currently collect and process the following information: \n•	Legal Name  \n•	National Insurance Number  \n•	Contact Info (Phone Number, Email, Address) \n\n (1) How we get the personal information and why we have it: \nWe collect personal information as it is needed, we don’t collect an unnecessary data. \n We collect important Identifier such as Name and Data of Birth as wee need to know who you are to make sure that pay is the right amount. \n We collect National Insurance Numbers to pay you correctly and make sure you are identified correctly. \n\n (2) Under the General Data Protection Regulation (GDPR), the lawful bases we rely on for processing this information are: \n (a) Your consent. You are able to remove your consent at any time. You can do this by contacting us directly (See contact details). \n (b) We have a contractual obligation. \n (c) We have a legal obligation. \n (d) We have a vital interest. \n (e) We need it to perform a public task. \n (f) We have a legitimate interest. \n\n (3) How we store your personal information: \n Your information is securely stored on a secure external database. \n We keep your personal information for as long as you are working for us. \n We will then dispose your information by writing over this data to make sure there is no trace of it left. \n If any data has been stored on paper, this is also destroyed. \n\n (4) Your data protection rights: \n Under data protection law, you have rights including: \n Your right of access - You have the right to ask us for copies of your personal information. \n Your right to rectification - You have the right to ask us to rectify personal information you think is inaccurate. \n You also have the right to ask us to complete information you think is incomplete. \n Your right to erasure - You have the right to ask us to erase your personal information in certain circumstances. \n Your right to restriction of processing - You have the right to ask us to restrict the processing of your personal information in certain circumstances. \n Your right to object to processing - You have the the right to object to the processing of your personal information in certain circumstances.\n Your right to data portability - You have the right to ask that we transfer the personal information you gave us to another organisation, \n or to you, in certain circumstances. \n You are not required to pay any charge for exercising your rights. If you make a request, we have one month to respond to you. \n Please contact us at admin@brainwireltd.com you wish to make a request.")

def DestroyHomePayslip():
    Home.withdraw()
    PayslipView()

def TOReq():
    global viewform
    viewform = Toplevel()
    viewform.title("Request Time Off")
    width = 1024
    height = 739
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    viewform.config(bg = "#81F7F3")

    #panel 
    Label(viewform, text="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=50).place(x=0, y=0)

    global tree    
    TopViewForm = Frame(viewform, width=600, bd=1, relief=FLAT, bg = "#81F7F3")
    TopViewForm.pack(side=TOP, fill=X)

    Tops= Frame(viewform, width= 1350, height= 50, bd=8, relief= FLAT, bg = "#81F7F3")
    Tops.pack(side=TOP)
    f1= Frame(viewform, width=600, height=600, bd=8, relief=FLAT, bg = "#81F7F3")
    f1.pack()

    f1a= Frame(f1, width=600, height= 200,bd=20, relief= FLAT, bg = "#81F7F3")
    f1a.pack(side=TOP)
    f1b= Frame(f1,width=600, height= 600, bd=20, relief= FLAT, bg = "#81F7F3")
    f1b.pack(side=TOP)
    lblinfo= Label(Tops, font=('arial',45), text="Request Time Off", bg ="white")
    lblinfo.grid(row=0, column=0, pady = 20)

    lblName= Label(f1a,text= "Name",relief=FLAT, bg = "#81F7F3", font=('arial',16,'bold'),bd=20).grid(row=0,column=0)
    lblAddress= Label(f1a,text= "Date",relief=FLAT,bg = "#81F7F3",font=('arial',16,'bold'),bd=20).grid(row=1,column=0)
    lblEmployer= Label(f1a,text= "Reason",relief=FLAT,bg = "#81F7F3",font=('arial',16,'bold'),bd=20).grid(row=2,column=0)

    etxtName1= Entry(f1a, textvariable= Name,font=('arial',8,'bold'),bd=16,width=22, justify='left', relief=FLAT)
    etxtName1.grid(row=0,column=1,pady=10)
    etxtDate= Entry(f1a,textvariable= Address,font=('arial',8,'bold'),bd=16, width=22, justify='left', relief=FLAT)
    etxtDate.grid(row=1,column=1,pady=10)
    etxtReason= Entry(f1a,textvariable= Employer,font=('arial',8,'bold'),bd=16, width=22, justify='left', relief=FLAT)
    etxtReason.grid(row=2,column=1,pady=10)

    #request time off button
    btn_requestTO = Button(f1a, text="Request", font=('arial', 18), width=30, bg="#01A9DB", command=RequestQ)
    btn_requestTO.grid(row=3, columnspan=2, pady=20)
    #request time off button
    btn_backB = Button(f1a, text="Back", font=('arial', 18), width=30, bg="#01A9DB", command=BackButtonRTO)
    btn_backB.grid(row=4, columnspan=2, pady=20) 

def RequestQ():
    result = tkMessageBox.askquestion('Request', 'Send request?', icon="warning")
    if result == 'yes':
        viewform.destroy()
        AssocMainHome()


#------------------------------------------------------------------------------
#admin login
def AdminLogin():
    global lbl_result
    Loginform = Toplevel()
    Loginform.title("Admin Login")
    width = 1024
    height = 739
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    Loginform.resizable(0, 0)
    Loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Loginform.configure( bg = "#81F7F3")
    TopLoginFormAssoc = Frame(Loginform, width=600, height=100, bd=1, relief=FLAT, bg = "#81F7F3")
    TopLoginFormAssoc.pack(side=TOP, pady=20)
    #login title
    lbl_text = Label(TopLoginFormAssoc, text="Admin Login", font=('arial', 45), bg = "white")
    lbl_text.pack(fill=X)

    MidLoginFormAssoc = Frame(Loginform, width=600, bg = "#81F7F3")
    MidLoginFormAssoc.pack(side=TOP, pady=50)
    #username label
    lbl_usernameAssoc = Label(MidLoginFormAssoc, text="Username:", font=('arial', 25), bd=18, bg = "#81F7F3", relief = FLAT)
    lbl_usernameAssoc.grid(row=0)
    #password label
    lbl_passwordAssoc = Label(MidLoginFormAssoc, text="Password:", font=('arial', 25), bd=18, bg = "#81F7F3", relief = FLAT)
    lbl_passwordAssoc.grid(row=1)
    #error label
    lbl_result = Label(MidLoginFormAssoc, text="", font=('arial', 18), bg = "#81F7F3", relief = FLAT)
    lbl_result.grid(row=3, columnspan=2)
    #username text input
    username = Entry(MidLoginFormAssoc, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    #password text input
    password = Entry(MidLoginFormAssoc, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    #login button
    btn_login = Button(MidLoginFormAssoc, text="Login", font=('arial', 18), width=30, bg="#01A9DB", command=DBAdminLogin)
    btn_login.grid(row=2, columnspan=2, pady=20)
    #back button
    btn_back = Button(MidLoginFormAssoc, text="Back", font=('arial', 18), width=30, bg="#01A9DB", command=BackButton)
    btn_back.grid(row=3, columnspan=2, pady=20)
    #privacy policy
    lbl_privacy = Button(MidLoginFormAssoc, text="By Logging in, you accept our Privacy Policy, click for more information",font=('arial', 14), bg = "#81F7F3", relief = FLAT, command=PrivacyPolicy)
    lbl_privacy.grid(row=4, columnspan=2)

    #astetics=======================================================
    #panel
    Label(Loginform, text ="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=60).place(x=0,y=0)
    #logo    
    lab = Label(TopLoginFormAssoc, image = my_logo_pic, bg="#81F7F3", relief = FLAT).pack()

def AdminDatabase():
    global conn, cursor
    conn = sqlite3.connect("plswork.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `employee` (emp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, emp_name TEXT, emp_addr TEXT, emp_ni TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def DBAdminLogin(event=None):

    global admin_id
    AdminDatabase()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            AdminMainHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()   

def DestroyOptionToAdminLog():
    loginformOptions.withdraw()
    AdminLogin()

def AdminMainHome():

    global Home
    Home = Toplevel()
    Home.title("Admin Home")
    width = 1024
    height = 739
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=FLAT)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Admin Home", font=('arial', 45), bg = "white")
    lbl_display.pack()

#astetics=======================================================
#panel
    Label(Home, text="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=60).place(x=0, y=0)   

#logo
    lab = Label(Home, image=my_logo_pic, bg="#81F7F3").pack()
#astetics=======================================================

#menu options
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit)
    filemenu2.add_command(label="Add new", command=DestroyOptionToShowNew)
    filemenu2.add_command(label="View", command=DestroyOptionView)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Employees", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#81F7F3")

def BackButtonPrivacy():

    Loginform.withdraw()

def BackButtonView():
    viewform.withdraw()
    AdminMainHome()

def BackButtonAddNew():
    addnewform.withdraw()
    AdminMainHome()

def BackButton():

    LoginForm()  

def BackButtonWages():
    payslipform.withdraw()
    AssocMainHome()

def BackButtonRTO():

    viewform.withdraw()
#------------------------------------------------------------------------------

#file menu options==================================================================================================================================================================================================
def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        AdminDatabase()
        cursor.execute("SELECT * FROM `employee` WHERE `emp_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def PayslipView():
    global payslipform
    payslipform = Toplevel()
    payslipform.title("View Payslip")
    width = 1024
    height = 739
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    payslipform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    payslipform.resizable(0, 0)
    payslipform.config(bg="#81F7F3")

    lbl_text = Label(payslipform, text="View Payslip", font=('arial', 45), bg = "white", relief = FLAT)
    lbl_text.pack(pady = 20)
    
    lblPaySlip=Label(payslipform, bg = "#81F7F3", font=('arial',20,'bold'),textvariable=DateOfOrder).pack()

    txtPaySlip= Text(payslipform, relief = "flat", bg = "#81F7F3", height=22, width=40,bd=16,font=('arial',12,'bold'))
    txtPaySlip.pack(side = TOP)
    lblName = Label(txtPaySlip, text = "Name:",fg = "green", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblName.grid(row = 0, column = 0)
    lbladdress = Label(txtPaySlip, text = "Address:",fg = "green", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lbladdress.grid(row = 0, column = 2)
    lblEmployer = Label(txtPaySlip, text = "Employer:",fg = "blue", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblEmployer.grid(row = 1, column = 0)
    lblNinumber = Label(txtPaySlip, text = "NI Number:",fg = "blue", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblNinumber.grid(row = 1, column = 2)
    lblhoursworked = Label(txtPaySlip, text = "Hours Worked:",fg = "red", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblhoursworked.grid(row = 2, column = 0)
    lblhourlyrate = Label(txtPaySlip, text = "Hourly Rate:",fg = "red", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblhourlyrate.grid(row = 2, column = 2)
    lbltax = Label(txtPaySlip, text = "Tax payable:",fg = "orange", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lbltax.grid(row = 3, column = 0)
    lblovertime = Label(txtPaySlip, text = "Extra Bonus:",fg = "orange", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblovertime.grid(row = 3, column = 2)
    lblgrosspay = Label(txtPaySlip, text = "Grosspay:", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblgrosspay.grid(row = 4, column = 0)
    lblNetpay = Label(txtPaySlip, text = "Net Pay:", font = ('arial',16,'bold'),bd = 20, bg = "#81F7F3")
    lblNetpay.grid(row = 4, column = 2)
    etxtname = Entry(txtPaySlip, textvariable = Name, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxtname.grid(row = 0, column = 1)
    etxtadd = Entry(txtPaySlip, textvariable = Address, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxtadd.grid(row = 0, column = 3)
    etxtemployer = Entry(txtPaySlip, textvariable = Employer, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxtemployer.grid(row = 1, column = 1)
    etxtnumber = Entry(txtPaySlip, textvariable = Ninumber, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxtnumber.grid(row = 1, column = 3)
    etxthoursw = Entry(txtPaySlip, textvariable = hoursworked, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxthoursw.grid(row = 2, column = 1)
    etxthourlyr = Entry(txtPaySlip, textvariable = hourlyrate, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxthourlyr.grid(row = 2, column = 3)
    etxttax = Entry(txtPaySlip, textvariable = tax, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxttax.grid(row = 3, column = 1)
    etxtovertime = Entry(txtPaySlip, textvariable = overtime, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxtovertime.grid(row = 3, column = 3)
    etxtnetpay = Entry(txtPaySlip, textvariable = netpay, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxtnetpay.grid(row = 4, column = 3)
    etxtpayable = Entry(txtPaySlip, textvariable = payable, font = ('arial',16,'bold'),bd = 16,width = 10, justify = 'left', relief = "flat")
    etxtpayable.grid(row = 4, column = 1) 
    
    btn_reset = Button(txtPaySlip, text="Calculate",font=('arial', 18), width=30, command=WeeklyWages, bg = "#01A9DB")
    btn_reset.grid(row = 5, columnspan = 2, column = 1)
    btn_reset = Button(txtPaySlip, text="Reset",font=('arial', 18), width=30, command=ResetWages, bg = "#01A9DB")
    btn_reset.grid(row = 6, columnspan = 2, column = 1)
    btn_back = Button(txtPaySlip, text="Back",font=('arial', 18), width=30, command=BackButtonWages, bg = "#01A9DB")
    btn_back.grid(row = 7, columnspan = 2, column = 1)


    #astetics=======================================================
    #panel 
    Label(payslipform, text="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=50).place(x=0, y=0)

def info():
    txtPaySlip.insert(END, "\t\tPay Slip\n\n")
    txtPaySlip.insert(END, 'Name:\t\t'+Name.get()+"\n\n")
    txtPaySlip.insert(END, 'Address:\t\t'+Address.get()+"\n\n")
    txtPaySlip.insert(END, 'Employer:\t\t'+Employer.get()+"\n\n")
    txtPaySlip.insert(END, 'NI Number:\t\t'+NINumber.get()+"\n\n")
    txtPaySlip.insert(END, 'HoursWorked:\t\t'+HoursWorked.get()+"\n\n")
    txtPaySlip.insert(END, 'NetPayable:\t\t'+NetPayable.get()+"\n\n")
    txtPaySlip.insert(END, 'Wages Per Hour:\t\t'+WagesHour.get()+"\n\n")
    txtPaySlip.insert(END,'Tax Paid:\t\t'+Taxable.get()+"\n\n")
    txtPaySlip.insert(END, 'Payable:\t\t'+ Payable.get()+"\n\n")
    return

def ResetWages():
    Name.set("")
    Address.set("")
    Employer.set("")
    Ninumber.set("")
    hoursworked.set("")
    hourlyrate.set("")
    tax.set("")
    overtime.set("")
    netpay.set("")
    payable.set("")
    return

def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("View Employees")
    width = 1024
    height = 739
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)

    global tree    
    TopViewForm = Frame(viewform, width=600, bd=1, relief=FLAT, bg = "#81F7F3")
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600, bg = "#81F7F3")
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600, bg = "#81F7F3")
    MidViewForm.pack(side = LEFT)
    lbl_text = Label(TopViewForm, text="View Employees", font=('arial', 18), bg = "white", relief = FLAT)
    lbl_text.pack()
    
    lab = Label(LeftViewForm, image=my_logo_pic, bg="#81F7F3").pack()
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15), bg = "#81F7F3")
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search, bg = "#01A9DB")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset, bg = "#01A9DB")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete, bg = "#01A9DB")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_back = Button(LeftViewForm, text="Back", command=BackButtonView, bg = "#01A9DB")
    btn_back.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("EmployeeID", "Employee Name", "Employee Address", "Employee NI"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('EmployeeID', text="EmployeeID",anchor=W)
    tree.heading('Employee Name', text="Employee Name",anchor=W)
    tree.heading('Employee Address', text="Employee Address",anchor=W)
    tree.heading('Employee NI', text="Employee NI",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def Logout():
    result = tkMessageBox.askquestion('Payroll System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        Home.destroy() 

def DestroyOptionToShowNew():
    Home.withdraw()
    ShowAddNew()

def DestroyOptionView():
    Home.withdraw()
    ShowView()

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add New Employee")
    width = 1024
    height = 739
    #panel
    Label(addnewform, text="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=60).place(x=0, y=0)
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addnewform.config(bg = "#81F7F3")

    TopAddNew = Frame(addnewform, bd=1, relief=FLAT)
    TopAddNew.pack(side=TOP, pady=10)
      
    lbl_text = Label(TopAddNew,bg = "white", text="Add New Employee", font=('arial', 45))
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600, bg = "#81F7F3")
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Employee Name:", font=('arial', 25), bd=10, bg = "#81F7F3")
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNew, text="Employee Address:", font=('arial', 25), bd=10, bg = "#81F7F3")
    lbl_qty.grid(row=1, sticky=W)
    lbl_price = Label(MidAddNew, text="Employee NI:", font=('arial', 25), bd=10, bg = "#81F7F3")
    lbl_price.grid(row=2, sticky=W)
    productname = Entry(MidAddNew, textvariable=emp_name, font=('arial', 25), width=15)
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddNew, textvariable=emp_ni, font=('arial', 25), width=15)
    productqty.grid(row=1, column=1)
    productprice = Entry(MidAddNew, textvariable=emp_addr, font=('arial', 25), width=15)
    productprice.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=20)
    btn_back = Button(MidAddNew, text="Back", font=('arial', 18), width=30, command=BackButtonAddNew, bg = "#01A9DB")
    btn_back.grid(row=4, columnspan=2, pady=20)

def AddNew():
    AdminDatabase()
    cursor.execute("INSERT INTO `employee` (emp_name, emp_addr, emp_ni) VALUES(?, ?, ?)", (str(emp_name.get()), str(emp_ni.get()), str(emp_addr.get())))
    conn.commit()
    emp_name.set("")
    emp_ni.set("")
    emp_addr.set("")
    cursor.close()
    conn.close()

def DisplayData():
    AdminDatabase()
    cursor.execute("SELECT * FROM `employee`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Payroll System', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            AdminDatabase()
            cursor.execute("DELETE FROM `employee` WHERE `emp_name` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Exit():
    result = tkMessageBox.askquestion('Payroll System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()

def WeeklyWages():

    Hoursworkedinweek = float(hoursworked.get())
    wageperhour = float(hourlyrate.get())
    pay = wageperhour * Hoursworkedinweek
    paydue = "£" ,str('%.2f' %(pay))
    payable.set(paydue)
    
    taxa = pay*0.2
    Taxable = "£" ,str('%.2f' %(taxa))
    tax.set(Taxable)
    
    netpaya = pay - taxa
    Netpays = "£" ,str('%.2f' %(netpaya))
    netpay.set(Netpays)
    
    if Hoursworkedinweek> 40:
        overtimehours = (Hoursworkedinweek - 40) + wageperhour *1.5
        overtimeh = "£" ,str('%.2f' %(overtimehours))
        overtime.set(overtimeh)
        
    elif Hoursworkedinweek<40:
        overtimepay = (Hoursworkedinweek-40) + wageperhour *1.5
        overtimeh = "£", str('%.2f' %(overtimepay))
        overtime.set(overtimeh)
    return

#Root=================================================================================================================================================================================================================#
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=filemenu)
filemenu.add_command(label="Login", command=DestroyFileToOption)
filemenu.add_command(label="Exit", command=Exit)
root.config(menu=menubar)

#FRAME
Title = Frame(root, bd=1, relief=FLAT)
Title.pack(pady=10)

#LABEL WIDGET IN OPENING SYSTEM
lbl_display = Label(Title, text="UFIX LTD Payroll", font=('ariel', 45), bg = "white")
lbl_display.pack()

#astetics=======================================================
#panel 
Label(root, text="Position 1 : x=0, y=0", bg="#01A9DB", fg="#01A9DB", height=50).place(x=0, y=0)

#logo
my_logo_pic = PhotoImage(file = "brainwirelogo.png")
lab = Label(root, image=my_logo_pic, bg="#81F7F3").pack()
#astetics=======================================================

#INITIALIZATION
if __name__ == '__main__':
    root.mainloop()