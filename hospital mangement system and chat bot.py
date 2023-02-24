import tabulate as tab
import mysql.connector as sql
mycon = sql.connect(host="localhost", user="root", passwd="puru9719", database="HOSPITAL")
    #if mycon.is_connected():
    #    print("succesfull connection")
cursor = mycon.cursor()
print("********************************************************")
print("*       \t\t\tHOSPITAL MANAGEMENT SYSTEM\t\t\t*")
print("********************************************************")
print("\n")
print("Detail analysis")
def det_doctor():
    print("Details of doctor * ")
    cursor.execute(" SELECT * FROM DOCTOR_INFO")
    data = cursor.fetchall()
    l = [["s.no", "Name", "Gender", "Designation", "Rating", "Spectialist", "Doctor_Code"]]
    for i in data:
        l.append(list(i))
    print(tab.tabulate(l, headers="firstrow"))
def det_patient():
    print("Details of patient * ")
    cursor.execute(" SELECT * FROM PATIENT")
    data2 = cursor.fetchall()
    l = [["S.no", "Name", "Date_Entered", "AGE","Date_Discharge", "Blood_Group", "Fees", "Due"]]
    for i in data2:
        l.append(list(i))
    print(tab.tabulate(l, headers="firstrow"))
def add_details():
    print("Add details of new patient in pateint table")
    sn=int(input("enter serial no.:"))
    n=input("enter name of patient:")
    da=input("date of entering(yyyy-mm-dd):")
    ag=int(input("enter the age of patient:"))
    dd=input("date of discharge(yyyy-mm-dd/0000-00-00):")
    bg=input("enter blood group:")
    fee=int(input("enter the  total fee:"))
    due=input("enter fee submited or not(y/n):")
    s="INSERT INTO PATIENT (S_NO,NAME,DATE_ENTERED,AGE,DATE_DISCHARGE,BLOOD_GROUP,FEES_LEFT,DUE)VALUES({},'{}','{}',{},'{}','{}',{},'{}')".format(sn,n,da,ag,dd,bg,fee,due)
    cursor.execute(s)
    mycon.commit()
def search():
    print("1.Search by NMAE:")
    print("2.Search by AGE:")
    print("3.Search by Blood Group:")
    print("4.search for Due Left:")
    n=int(input("enter your choice NO.:"))
    if (n==1):
        N=input("Enter the name u want to search: ")
        s="SELECT * FROM PATIENT WHERE NAME = %s"
        t=(N,)
        cursor.execute(s,t)
        data=cursor.fetchall()
        l = [["S.no", "Name", "Date_Entered","AGE", "Date_Discharge", "Blood_Group", "Fees", "Due"]]
        for i in data:
            l.append(list(i))
        print(tab.tabulate(l, headers="firstrow"))
    elif(n==2):
        age=int(input("Enter the age group people u want to search: "))
        st="SELECT * FROM PATIENT WHERE AGE =%s"
        t = (age,)
        cursor.execute(st,t)
        data=cursor.fetchall()
        l = [["S.no", "Name", "Date_Absorb","AGE", "Date_Discharge", "Blood_Group", "Fees", "Due"]]
        for i in data:
            l.append(list(i))
        print(tab.tabulate(l, headers="firstrow"))
    elif(n==3):
        bg=input("Enter the blood group  people u want to search: ")
        st="SELECT * FROM PATIENT WHERE BLOOD_GROUP =%s"
        t = (bg,)
        cursor.execute(st,t)
        data=cursor.fetchall()
        l = [["S.no", "Name", "Date_Absorb","AGE", "Date_Discharge", "Blood_Group", "Fees", "Due"]]
        for i in data:
            l.append(list(i))
        print(tab.tabulate(l, headers="firstrow"))
    elif(n==4):
        due=input("Enter the Y/N for people dues left or not that is to be want to search: ")
        st="SELECT * FROM PATIENT WHERE DUE =%s"
        t = (due,)
        cursor.execute(st,t)
        data=cursor.fetchall()
        l = [["S.no", "Name", "Date_Absorb","AGE", "Date_Discharge", "Blood_Group", "Fees", "Due"]]
        for i in data:
            l.append(list(i))
        print(tab.tabulate(l, headers="firstrow"))
    else:
        print("\nWrong input! See the list again.\n")
def edit():
    print("0.Edit Serial No. :")
    print("1.Edit NMAE:")
    print("2.Edit by AGE:")
    print("3.Edit Blood Group:")
    print("4.Edit Due Fees:")
    print("5.Edit Date of Discharge:")
    print("6.Edit Due Left ")
    n=int(input("enter your choice NO.:"))
    if (n==0):
        x=int(input("enter the serial no.:"))
        y=input("enter the name at which u want to do correction [in CAPITAL] :")
        st="UPDATE PATIENT SET S_NO =%s WHERE NAME = %s"
        tp=(x,y)
        cursor.execute(st,tp)
        mycon.commit()
    elif(n == 1):
        y = input("enter the name which u want to correct[in CAPITAL] :")
        x = int(input("enter the serial no. at which u want to do correction:"))
        st = "UPDATE PATIENT SET NAME = %s WHERE S_NO = %s"
        tp=(y,x)
        cursor.execute(st,tp)
        mycon.commit()
    elif (n == 2):
        y =int(input("enter the age u want to edit :"))
        x = input("enter the name at which u want to do correction [in CAPITAL]:")
        st = "UPDATE PATIENT SET AGE = %s WHERE NAME = %s"
        tp = (y, x)
        cursor.execute(st, tp)
        mycon.commit()
    elif (n == 3):
        y = input("enter the blood group u want to edit :")
        x = input("enter the name at which u want to do correction [in CAPITAL]:")
        st = "UPDATE PATIENT SET BLOOD_GROUP = %s WHERE NAME = %s"
        tp = (y, x)
        cursor.execute(st, tp)
        mycon.commit()
    elif (n == 4):
        y = int(input("enter the due fee u want to edit :"))
        x = input("enter the name at which u want to do correction [in CAPITAL]:")
        st = "UPDATE PATIENT SET FEES_LEFT= %s WHERE NAME = %s"
        tp = (y, x)
        cursor.execute(st, tp)
        mycon.commit()
    elif (n == 5):
        y = input("enter the date of discharge u want to edit[yyyy-mm-dd] :")
        x = input("enter the name at which u want to do correction [in CAPITAL]:")
        st = "UPDATE PATIENT SET DATE_DISCHARGE = %s WHERE NAME = %s"
        tp = (y, x)
        cursor.execute(st, tp)
        mycon.commit()
    elif(n == 6):
        y = input("enter the Y/N u want to edit  in due left or not:")
        x = input("enter the name at which u want to do correction [in CAPITAL]:")
        st = "UPDATE PATIENT SET DUE = %s WHERE NAME = %s"
        tp = (y, x)
        cursor.execute(st, tp)
        mycon.commit()
def bill():
    due = input(" Enter the name of patient whose fees left u want to see: ")
    st = "SELECT S_NO,NAME,FEES_LEFT,DUE FROM PATIENT WHERE NAME =%s"
    t = (due,)
    cursor.execute(st, t)
    data = cursor.fetchall()
    l = [["S.no", "Name", "Fees", "Due"]]
    for i in data:
        l.append(list(i))
    print(tab.tabulate(l, headers="firstrow"))
def chatbot():
    import chatbot2
while (True):
    print("\n1.Show Dteails of doctor")
    print("2.Show Dteails of pateint")
    print("3.Add Dteails of patient")
    print("4.Edit Dteails of patient ")
    print("5.Search Dteails of patient by his/her name")
    print("6.Show bill of respective person")
    print("7.Concult  with doctor using chatbot")
    print("8.Exit\n")
    n=int(input("enter the choice NO.: "))
    print("\n")
    if(n==1):
        det_doctor()
    elif(n==2):
        det_patient()
    elif(n == 3):
        add_details()
    elif(n==4):
        edit()
    elif(n == 5):
        search()
    elif(n==6):
        bill()
    elif(n==7):
        chatbot()
    elif(n==8):
        break
    else:
        print("***********invalid input************")
print("u are out off loop !thanku for acessing")
