'''
structure:
slno
itemID
Get the name from inventory
quantity
Discounts whole dict

Inventory structure:
Item ID
Name
Total amount
Discounts {k%}


Client Structure:
Client ID
Client Phone No.
Client Name
Client Discount 

We only write to ledger, but frequently search around the inventory
'''
from abc import ABC
from datetime import datetime
from glob import glob
import shutil
from tkinter import *
from tkinter.messagebox import ABORT 
from tkinter.ttk import *

master = Tk()
master.geometry("400x300")

CurrBillList=[]
InventoryList= []
ClientList=[]
TotalBillList =[]


def ClientLoginChecker(Page,ID,Phno):
    global ClientList
    for i in ClientList:
        if(i[0] == ID):
            if(i[1][-4:]==Phno):
                NormalCalc(i)
                return None
            else:
                msg =Message(Page,"Phone No is Invalid")
                msg.grid(row = 2, column = 3, sticky = E)
    msg =Message(Page,"Invalid ID No")
    msg.grid(row = 2, column = 3, sticky = E)
    return None

def ClientLogin():
    ClientPage=Toplevel(master)
    ClientPage.title("Login to client")
    ClientPage.geometry("800x600")
    lCL0 = Label(ClientPage,text = "Login to Client")
    lCL1 = Label(ClientPage, text = "Client ID:")
    lCL2 = Label(ClientPage, text = "Client Phone No last 4 digits:")
 
    lCL0.grid(row = 0, column =1,sticky = N)
    lCL1.grid(row = 2, column = 0, sticky = N, pady = 2)
    lCL2.grid(row = 3, column = 0, sticky = N, pady = 2)

    eCl1 = Entry(ClientPage)
    eCl2 = Entry(ClientPage)

    eCl1.grid(row = 2, column = 1, pady = 2)
    eCl2.grid(row = 3, column = 1, pady = 2)

    bCl1 = Button(ClientPage,text = "Login Client",command = lambda: ClientLoginChecker(ClientPage,eCl1.get(),eCl2.get()))
    bCl1.grid(row = 4, column = 0, pady = 2)
    bCl5 = Button(ClientPage,text = "Logout Client",command =lambda: ClientPage.destroy)
    bCl5.grid(row = 4, column = 1, pady = 2)

def addlist(Page,ID,QTY):
    global InventoryList, CurrBillList
    DetID = next((item for item in InventoryList if item["ID"] == ID), None)
    if DetID is None:
        msg =Message(Page,"Invalid ID No")
        msg.grid(row = 2, column = 3, sticky = E)
        return None
    if QTY> DetID["Quantity"]:
        msg =Message(Page,"Only"+DetID["Quantity"]+"Present")
        msg.grid(row = 2, column = 3, sticky = E)
        QTY= DetID["Quantity"]
    new = {"slno":len(CurrBillList)+1,"ItemID":ID,"Name":DetID["Name"],"Quantity":QTY,"Discounts":DetID["Discount"]}

def NormalCalc(i):
    NormalPage =Toplevel(master)
    if i is not None:
        NormalPage.title("Take the list For Client"+i["ID"])
    else:
        NormalPage.title("Take the list")
    NormalPage.geometry("800x600")
    lNB0 = Label(NormalPage,text = "Enter the Items")
    lNB1 = Label(NormalPage,text = "Item ID")
    lNB2 = Label(NormalPage,text = "Quantity")

    lNB0.grid(row = 0, column =1,sticky = N)
    lNB1.grid(row = 2, column = 0, sticky = N, pady = 2)
    lNB2.grid(row = 2, column = 1, sticky = N, pady = 2)

    TNB1 = Entry(NormalPage)
    TNB2 = Entry(NormalPage)

    TNB1.grid(row = 3, column = 0, sticky = N, pady = 2)
    TNB2.grid(row = 3, column = 1, sticky = N, pady = 2)

    TBNB0 = Text(NormalPage,height = 5, width = 52)

    bNB1 = Button(NormalPage,text = "Add to list",command = lambda:addlist(NormalPage,TBNB0,TNB1.get(),TNB2.get()))
    bNB1.grid(row = 4, column = 0, sticky = N, pady = 2)

    TBNB0.grid(row = 5, column = 0, sticky = N, pady = 2)
def openNewWindow():
    ChoicePage = Toplevel(master)
    ChoicePage.title("Choose Operation")
    ChoicePage.geometry("800x600")
    bC1 = Button(ChoicePage,text = "Client Login",command = ClientLogin)
    bC1.grid(row = 0, column = 0, sticky = N)
    bC2 = Button(ChoicePage,text = "Clientless Login",command = lambda: NormalCalc(None))
    bC2.grid(row = 0, column = 1, sticky = N)
#openNewWindow
def DestroyLogin():
    lm0.destroy()
    lm1.destroy()
    lm2.destroy()
    em1.destroy()
    em2.destroy()
    bm1.destroy()
#DestroyLogin
def OpenBook(op,BkLoc):
    try:
        Book = open(BkLoc+".bin","r+")
        T =datetime.now().strftime("%H%M%S")
        if(op is None):
            try:
                shutil.copyfile(BkLoc+".bin",BkLoc+"{}.bin".format(T))
                print(BkLoc+"backup time is",T)
            except:
                print(BkLoc+"copy Not Working")
        else:
             Store=Book.readlines()
             print(BkLoc+" backup +store time is",T)
        Book.close()
        return Store
    except:
        print(BkLoc+" not opened")
        exit()
#OpenBook
def LoginChecker():
    global InventoryList,ClientList
    try:
        empfile =open("employees.bin","r")
        print("Employee file read time is",datetime.now().strftime("%H%M%S"))
    except:
         print("file not opened")
    ThisEMP = em1.get()
    ThisEMPPwd = em2.get()
    FOUND=0
    while FOUND == 0:
        a = empfile.readline()
        if len(a) == 0:
            print("The EMPID does not exist , retry")
            empfile.close()
            exit()
        else:
            a=a.split(" ")
            if ThisEMP == a[0] and ThisEMP[0] in ['E','M'] :
                FOUND == 1
                if ThisEMPPwd == a[1].strip() :
                    print("Success")
                    openNewWindow()
                    InventoryList=OpenBook("ADD","Inventory")
                    OpenBook(None,"Ledger")
                    ClientList=OpenBook("ADD","ClientList")
                    DestroyLogin()
                    return None
                else:
                    print("Wrong PWD, retry")
                    exit()
            elif ThisEMP[0] != 'E':
                print("Access Denied")
                exit()
            else:
                continue
    empfile.close()
#LoginChecker
def CloseApp():
    global InventoryList,TotalBillList
    try:
        empfile =open("Inventory.bin","w")
        print("Inventory file write time is",datetime.now().strftime("%H%M%S"))
        for item in InventoryList:
            empfile.write(item)
        empfile.close()    
    except:
         print("file not opened")
    try:
        empfile =open("Ledger.bin","w")
        print("Inventory file write time is",datetime.now().strftime("%H%M%S"))
        for A in TotalBillList:
            for item in A:
                empfile.write(item)
        empfile.close()    
    except:
         print("file not opened")
    master.destroy()

if __name__ == "__main__":

    master.protocol("WM_DELETE_WINDOW", CloseApp)

    lm0 = Label(master,text = "Login to Point Of Sale Terminal")
    lm1 = Label(master, text = "Employee ID:")
    lm2 = Label(master, text = "Employee Password:")
 
    # grid method to arrange labels in respective
    # rows and columns as specified
    lm0.grid(row = 0, column =1,sticky = N)
    lm1.grid(row = 2, column = 0, sticky = N, pady = 2)
    lm2.grid(row = 3, column = 0, sticky = N, pady = 2)
 
    # entry widgets, used to take entry from user
    em1 = Entry(master)
    em2 = Entry(master)
 
    # this will arrange entry widgets
    em1.grid(row = 2, column = 1, pady = 2)
    em2.grid(row = 3, column = 1, pady = 2)

    bm1 = Button(master,text = "Login",command = LoginChecker)
    bm1.grid(row = 4, column = 0, pady = 2)
    bm5 = Button(master,text = "Logout",command = master.destroy)
    bm5.grid(row = 4, column = 1, pady = 2)
    #main

mainloop()