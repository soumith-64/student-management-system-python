import random
from time import sleep
import os
def display_menu():
    opt=[1,2,3,4,5,6]
    choice=0
    while True:
        print()
        print("#########---Student Management System Welcomes You 🤝 ---#########")
        print("")
        print("To Add Student press - 1 ")
        print("To View Student press - 2")
        print("To Search Student press - 3")
        print("To Update Student press - 4")
        print("To Delete Student press - 5")
        print("To Exit press - 6")
        try:
            print("")
            choice=int(input("Enter you choice : "))
            print()
        except ValueError:
            print("Please enter only number from 1 to 5 as per menue")
            continue

        if choice in opt:
            if choice==1:
                add_students()
            elif choice==2:
                view_students()
            elif choice == 3:
                result = search_students()
                if result is not None:
                    display_std(*result) # Passes the whole tuple of data
            elif choice==4:
                    update_students()
            elif choice==5:
                delete_students()
            else:
                print("Thanks for using me, Let me manage your students again")
                print("Saving DATA and Closing Application")
                sleep(2.3)
                break
        else:
            print("Enter a valid option")
            print("Returning to main menu")
            sleep(1.5)
            continue

def std_inp():  
    while True:
        try:
            print()
            roll_num = int(input("Enter roll number : "))
            print()
            name = input("Enter Name : ")
            print()
            age = int(input("Enter Age : "))
            print()
            dept = input("Enter Department : ").upper()
            print()
            py_mark = float(input("Enter Python mark : "))
            print()
            math_mark = float(input("Enter Math Mark : "))
            print()
            eng_mark = float(input("Enter English Mark : "))
            return roll_num, name, age, dept, py_mark, math_mark, eng_mark
        except ValueError:
            print("\nShould enter only valid form for each entity")
            print("Restarting student details entry...")
            sleep(1.5)



def calculate_total(py_mark,math_mark,eng_mark):

    total_mark = py_mark + math_mark + eng_mark
    return total_mark

def calculate_average(total_mark):
    if total_mark > 0 :
        avg=round(total_mark/3,2)
        return avg
    else:
        print()
        print("Are you sure all mark are zero : ")
        cf=int(input("If yes press 1 else 0 : "))
        if cf == 1:
            avg=0
            return avg
        else:
            print()
            print("Sorry then Enter detail from first :")
            print("redirecting......")
            sleep(1.5)
            add_students()



def calculate_grade(avg):

    grade=""

    if avg>=90:
        grade='A+'
    elif avg>=80 and avg<90:
        grade='A'
    elif avg>=70 and avg<80:
        grade='B'
    elif avg>=60 and avg<70:
        grade='C'
    elif avg>=50 and avg<60:
        grade='D'
    else:
        grade='F'
    return grade


def calculate_status(py_mark,math_mark,eng_mark):
    PoF=""
    if py_mark>=35 and math_mark>=35 and eng_mark>=35:
        PoF="Pass"
    else:
        PoF="Fail"
    return PoF


def save_student(roll_num,name,age,dept,py_mark,math_mark,eng_mark,total_mark,avg,grade,PoF):

    Std_detail_compressed="|".join(str(x) for x in [roll_num,name,age,dept,py_mark,math_mark,eng_mark,total_mark,avg,grade,PoF])

    with open("student.txt","a+") as stdinp:
            f=0
            stdinp.seek(0)
            for i in stdinp:

                if not i.strip():
                    continue

                check_lst=list(i.strip().split("|"))

                if int(check_lst[0])==roll_num:
                    print()
                    print(f"Sorry the roll number {roll_num} is already registred")
                    print()
                    print("Redirecting back to main menu...........")
                    f=1
                    break
            if f == 1:
                return False
            elif f == 0:
                stdinp.write(f"{Std_detail_compressed}\n")
                print()
                print("Student added sucessful, Redirecting........")
                return True


def add_students():
    print()
    print("Hi admin are you ready to fill the details")

    while True:

        #Getting input and storing in data in variable 
        roll_num,name,age,dept,py_mark,math_mark,eng_mark = std_inp()
        # here we are calculating the total
        total=calculate_total(py_mark,math_mark,eng_mark)
        #here we are calling the avg calculating function and storing the data
        avg=calculate_average(total)
        #here we are calling the grade calculating function and storing the data
        grd=calculate_grade(avg)
        #here we are calling the status calculating function and storing the data
        status=calculate_status(py_mark,math_mark,eng_mark)
        #here we are calling the save student calculating function and storing the data
        saved=save_student(roll_num,name,age,dept,py_mark,math_mark,eng_mark,total,avg,grd,status)

        if saved:
            break
# a function to display std details
def display_std(rollnum, name, age, dept, pymark, mathmark, engmark, total, avg, grade, status):
    print("\n")
    print("════════════════════════════════════════════════════════════════")
    print("                        STUDENTS DETAILS                        ")
    print("════════════════════════════════════════════════════════════════\n")
    print(f"Roll Number : {rollnum}\n")
    print(f"Name : {name}\n")            
    print(f"Age : {age}\n")                        
    print(f"Department : {dept}\n")                        
                                
    print(f"Python Marks : {pymark}\n")                        
    print(f"Math Marks   : {mathmark}\n")                        
    print(f"English Marks: {engmark}\n")                        
                                
    print("________________________________________________________________\n")              

    print(f"Total : {total}\n")                        
    print(f"Average : {avg}\n")                        
    print(f"Grade : {grade}\n")                        
    print(f"Status : {status}\n")                                                                       
    print("════════════════════════════════════════════════════════════════ \n")

#here now i am creating a student view function
def view_students():
    if os.path.exists("student.txt"):
        #reading the file and extracting the datas
        with open("student.txt","r") as read_std:
            read_std.seek(0)
            lines=read_std.readlines()
            valid_line=[lin.strip() for lin in lines if lin.strip()]
            if valid_line:
                i=1
                for line in valid_line:
                
                    dtls=list(line.strip().split("|"))
                    (
                     rollnum, name, age, dept,
                     pymark, mathmark, engmark,
                     total, avg, grade, status
                    ) = dtls
                    display_std(rollnum, name, age, dept,pymark, mathmark, engmark, total, avg, grade, status)              
                    i+=1
                    sleep(1)
                print("")
                print("All students data displayed \n")
                sleep(.7)
                print("Back to menu\n")
                sleep(.7)
                print("Redirecting........\n")
                sleep(2)
            else:
                    print("Sorry there is no data to fetch... \n")
                    sleep(.7)
                    print("Try adding some data and try again\n")
                    sleep(.7)
                    print("Back to main menu\n")
                    sleep(.7)
                    print("Rerdirecting............\n")
        sleep(1.3)
    else:
        print("Sorry there is no data to fetch... \n")
        sleep(.7)
        print("Try adding some data and try again\n")
        sleep(.7)
        print("Back to main menu\n")
        sleep(.7)
        print("Rerdirecting............\n")
        sleep(1.3)



def search_students():

    try:
        roll_num=int(input("Enter the roll number of the student :"))
    except ValueError:
        print("Enter a vaild number only\n")
        print("Enter again")
        sleep(1.2)
        return None

    if os.path.exists("student.txt"):
        with open("student.txt","r") as search_std:
            search_std.seek(0)
            #getting all line in the txt doc into a list for easy calculation
            lines=search_std.readlines()
            #storing line in list
            valid_line=[line.strip() for line in lines if line.strip()]
            #checking if the file has some data or not
            if valid_line:
                found=False
                for std_data in valid_line:
                    dts=std_data.strip().split("|")
                    if len(dts) == 11:
                        (
                            rollnum, name, age, dept,
                            pymark, mathmark, engmark,
                            total, avg, grade, status
                        ) = dts
                    else:
                        print("Skipping the data row...")
                    if int(rollnum) == roll_num:
                            found=True
                            break
                    
                if found:
                    return rollnum, name, age, dept, pymark, mathmark, engmark, total, avg, grade, status
                else:
                    print("")
                    print(f"Sorry no student found with this roll number {roll_num}")
                    return None
            else:
                print("Sorry there is no data to fetch... \n")
                sleep(.7)
                print("Try adding some data and try again\n")
                sleep(.7)
                print("Back to main menu\n")
                sleep(.7)
                print("Rerdirecting............\n")
                sleep(1.3)
                return None

def update_inp(data):

    print()
    print("To update value type else prese enter\n")
    try:
        rollnum = data[0]
        name = input(f"Original value is {data[1]} :: Type new value if needed : ").strip() or data[1]
        age = int(v) if (v := input(f"Original value is {data[2]} :: Type new value if needed : ").strip()) else data[2]
        dept = input(f"Original value is {data[3]} :: Type new value if needed : ").strip() or data[3]
        pymark = int(v) if (v := input(f"Original value is {data[4]} :: Type new value if needed : ").strip()) else data[4]
        mathmark = int(v) if (v := input(f"Original value is {data[5]} :: Type new value if needed : ").strip()) else data[5]
        engmark = int(v) if (v := input(f"Original value is {data[6]} :: Type new value if needed : ").strip()) else data[6]
        total=calculate_total(pymark, mathmark, engmark)
        avg=calculate_average(int(total))
        new_data = [
            str(rollnum), str(name), str(age), str(dept), 
            str(pymark), str(mathmark), str(engmark), 
            str(total), str(avg), str(calculate_grade(avg)), str(calculate_status(pymark, mathmark, engmark))
        ]  
    except ValueError:
        print("Age and marks must be numeric. Update cancelled.")
        return
    return new_data

def update_students():
    try:
        rollnum=int(input("Enter the roll number : "))
    except ValueError:
        print("Only enter roll number")
        print("Try again..........")
        sleep(1.2)
        return

    if not os.path.exists("student.txt"):
        print("Data file 'student.txt' not found. 😔")
        return
    with open("student.txt","r") as val_std:
        f=False
        lines=val_std.readlines()
        updated_line=[]
        for line in lines:
            if not line.strip():
                updated_line.append(line)
                print("Sorry empty line found 😔 ")
                continue
            data=line.strip().split("|")
            if int(data[0])==rollnum:
                datas=update_inp(data)
                updated_line.append("|".join(datas)+"\n")
                f=True
            else:
                updated_line.append(line)
    if f:
        with open("student.txt","w") as updt_std:
            for value in updated_line:
                updt_std.write(value)
        print()
        print("Value updated sucessfully 👍")
    else:
        print("Sorry no data 😔")
     

def delete_students():
    print("Comming soon 😶")

display_menu()