def CreatePwd(Txt):
    letters ="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ''.join(random.choice(letters) for i in range(6))
    Txt.delete(0,END)
    Txt.insert(0,password)

def EditEmployee():
    EditPage = Toplevel(master)
    EditPage.title("Edit Employee")
    EditPage.geometry("800x600")
    lAE0 = Label(EditPage,text = "Enter Employee Details")
    lAE1 = Label(EditPage, text = "Employee ID:")
    lAE2 = Label(EditPage, text = "Employee Password")
 
    # grid method to arrange labels in respective
    # rows and columns as specified
    lAE0.grid(row = 0, column =1,sticky = N)
    lAE1.grid(row = 2, column = 0, sticky = N, pady = 2)
    lAE2.grid(row = 3, column = 0, sticky = N, pady = 2)
 
    # entry widgets, used to take entry from user
    eAE1 = Entry(EditPage)
    eAE2 = Entry(EditPage)
 
    # this will arrange entry widgets
    eAE1.grid(row = 2, column = 1, pady = 2)
    eAE2.grid(row = 3, column = 1, pady = 2)

    bAE1 = Button(EditPage,text = "Create Random Password",command = lambda: CreatePwd(eAE2))
    bAE1.grid(row = 4, column = 0, pady = 2)
    bAE2 = Button(EditPage,text = "Apply Change in Password",command =lambda: CreateEditDel(EditPage,eAE1.get(),eAE2.get(),"EDIT"))
    bAE2.grid(row = 4, column = 1, pady = 2)
    bAE3 = Button(EditPage,text = "Delete Employee",command =lambda: CreateEditDel(EditPage,eAE1.get(),eAE2.get(),"DELETE"))
    bAE3.grid(row = 4, column = 2, pady = 2)
    bAE4 = Button(EditPage,text = "Close Window",command =EditPage.destroy)
    bAE4.grid(row = 4, column = 3, pady = 2)

def CloseApp():
    try:
        empfile =open("employees.bin","w")
        print("Employee file write time is",datetime.now().strftime("%H%M%S"))
        print("HERE?")
        for item in EMPDETLIST:
            empfile.write(item)
        empfile.close()    
    except:
         print("file not opened")
    master.destroy()

if __name__ == "__main__":
    master.protocol("WM_DELETE_WINDOW", CloseApp)

    lm0 = Label(master,text = "Login to Employee Manager")
    lm1 = Label(master, text = "Manager ID:")
    lm2 = Label(master, text = "Manager Password:")
 
    lm0.grid(row = 0, column =1,sticky = N)
    lm1.grid(row = 2, column = 0, sticky = N, pady = 2)
    lm2.grid(row = 3, column = 0, sticky = N, pady = 2)
 
    em1 = Entry(master)
    em2 = Entry(master)
 
    em1.grid(row = 2, column = 1, pady = 2)
    em2.grid(row = 3, column = 1, pady = 2)

    bm1 = Button(master,text = "Login",command = LoginChecker)
    bm1.grid(row = 4, column = 0, pady = 2)
    bm5 = Button(master,text = "Logout",command = CloseApp)
    bm5.grid(row = 4, column = 1, pady = 2)
    mainloop()