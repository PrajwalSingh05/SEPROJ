from datetime import datetime

EMPLOC = "B:\sem5\SE\PROJECT\MainProject\employees.bin"
LEDGLOC ="B:\sem5\SE\PROJECT\MainProject\Ledger.bin"
LEDGECPY ="B:\sem5\SE\PROJECT\MainProject\Ledger.bin.bk"


#first take the login ID and password for the employee and check against the data
try:
    empfile =open("employees.bin","r")
    print("Employee file read time is",datetime.now().strftime("%H%M%S"))
except:
    print("file not opened")

ThisEMP = input("Enter the employee ID ")
ThisEMPPwd = input("Enter your PWD ")

FOUND=0
while FOUND == 0:
    a = empfile.readline()
    if len(a) == 0:
        print("The EMPID does not exist , retry")
        empfile.close()
        exit()
    else:
        a=a.split(" ")
        if ThisEMP == a[0] :
            FOUND == 1
            if ThisEMPPwd == a[1].strip() :
                print("Success")
                break
            else:
                print("Wrong PWD, retry")
                exit()
        else:
            continue
empfile.close()

try:
    Ledger = open("Ledger.bin","r+")
    T =datetime.now().strftime("%H%M%S")

    LedgerBk = open("Ledger{}.bin".format(T),"w")
    text =Ledger.readlines()

    LedgerBk.writelines(text)
    LedgerBk.close()
    print("Ledger backup time is",T)

except:
    print("file not opened")



#EmpName = input("Enter the employee ID")
#EmpPwd = input("Enter the employee PWD")
#empfile.writelines(EmpName + " " + EmpPwd)
List = []
ListAll = []
inp = "y"

while True:
    
    if inp == "y":
        CustID =input("Enter Customer ID :")
        Item= input("Enter the item name :")
        price = input("Enter the price :")
        List.append([CustID,Item,price]) 
        inp = input("y to continue, else end list and calculate: ")
        L = "The Bill for "+str(CustID)+" at time"+str(datetime.now().strftime("%H:%M:%S"))+"\n"
        sum1=0
        for i in List:
            if i[0]==CustID:
               k= int(i[2])
               #print(i[1]," ------ ",k)
               L = L+str(i[1])+" ------ "+str(k)
               sum1 =sum1 + k
        L = L+"Total is "+str(sum1)+"\n"
        file1 = open("myfile.txt","a")
        file1.writelines(L)
        file1.close()
        print(L)
        continue
    else:
        CustID =input("Enter Customer ID :")
        sum = 0
        print("The Bill for "+CustID+" at time"+datetime.now().strftime("%H:%M:%S"))
        
        print("------------------------------------------------------------------")
        for i in List:
            if i[0]==CustID:
               k= int(i[2])
               print(i[1]," ------ ",k)
               sum =sum + k
        print("Total is ",sum)



Ledger.close()

