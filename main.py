from dataclasses import fields
from msilib.schema import AppSearch
import os
import re

from numpy import ascontiguousarray
from OOPS_Project import Admission
import csv
import pandas as pd

clear = lambda: os.system('cls')

def main_menu():
    clear()
    print(" Kristu Jayanti College ".center(146, '-'))
    print("\nWelcome to our User-Interface.")
    ans = int(input("\nPlease enter the option number you desrire to continue with\n\n1. Admissions\n2. ID Card\n3. Examinations\n4. Attendence\n5. Library\n6. Co-Curricular Activities\n7. Exit\n\nEnter your option: "))
    response(ans)

def response(n):
    if n == 1:
        admission()
    elif n == 2:
        pass
    elif n == 3:
        pass
    elif n == 4:
        pass
    elif n == 5:
        pass
    elif n == 6:
        pass
    elif n == 7:
        exit()


def admission():

    def apply():
        clear()
        print(" Application Form ".center(133, '-'))
        fname = input("Enter your first name : ")
        lname = input("\nEnter your last name : ")
        ag = 0
        while(ag == 0):
            ans1 = int(
                input("\nEnter your gender \n1. Male \n2. Female\nEnter the option number : "))
            if ans1 == 1:
                gender = "Male"
                ag = 1

            elif ans1 == 2:
                gender = "Female"
                ag = 1
                
            else:
                print("\nEnter a valid option number")
                
        dob = input("\nEnter your DOB in DD/MM/YYYY format : ")
        condition = True
        while (condition):
            p = r"\d{2}/\d{2}/\d{4}"
            result = re.findall(p, dob)
            if len(result) > 0:
                break
            else:
                print("\nInvalid format !")
                
        phoneno = input("\nEnter your Phone No. : ")
        while (len(phoneno) != 10 or phoneno.isdigit() == False):
            print("\nEnter a valid phome number")
            phoneno = input("\nEnter your Phone No. : ")

        emailid = input("\nEnter your Email-ID : ")
        while (emailid.endswith(".com") == False or "@" not in emailid):
            print("\nPlease enter a valid Email ID")
            emailid = input("\nEnter your Email ID : ")

        address = input("\nEnter your address : ")
        father_name = input("\nEnter your Father's name : ")
        father_occupation = input("\nEnter your Father's occupation : ")
        mother_name = input("\nEnter your Mother's name : ")
        mother_occupation = input("\nEnter your Mother's occupation : ")
        ac = 0
        while(ac == 0):
            ans2 = int(input(
                "\nSelect your Category \n1. General\n2. SC|ST\n3. 2B\n4. 3B\nEnter option number :  "))
            if ans2 == 1:
                category = "General"
                ac = 1
            elif ans2 == 2:
                category = "SC|ST"
                ac = 1
            elif ans2 == 3:
                category = "2B"
                ac = 1
            elif ans2 == 4:
                category = "3B"
                ac = 1
            else:
                print("\nEnter a valid option number")
                
        tenth_score = int(input("\nEnter your 10th grade marks (in percentage %) : "))
        twelveth_score = int(input("\nEnter your 12th grade marks (in percentage %) :  "))
        aps = 0
        while(aps == 0):
            ans3 = int(input("\nSelect your previous stream \n1. Science\n2. Commerce\n3. Arts\nEnter option number : "))
            if ans3 == 1:
                previous_stream = "Science"
                aps = 1
            elif ans3 == 2:
                previous_stream = "Commerce"
                aps = 1
            elif ans3 == 3:
                previous_stream = "Arts"
                aps = 1
            else:
                print("\nEnter a valid option")

        aos = 0
        while(aos == 0):
            ans4 = int(input("\nSelect the stream you want to opt for \n1. Science\n2. Commerce\n3. Arts\nEnter option number : "))
            if ans4 == 1:
                stream_opting_for = "Science"
                aos = 1
            elif ans4 == 2:
                stream_opting_for = "Commerce"
                aos = 1
            elif ans4 == 3:
                stream_opting_for = "Arts"
                aos = 1
            else:
                print("\nEnter a valid option")
                
        if stream_opting_for == "Science":
            asc = 0
            while(asc == 0):     
                ans5 = int(input("\nSelect the course your opting for : \n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\nEnter option number : "))
                if ans5 == 1:
                    course_opting_for = "BCA"
                    asc = 1
                elif ans5 == 2:
                    course_opting_for = "BCA in Analytics"
                    asc = 1
                elif ans5 == 3:
                    course_opting_for = "BSc(PMCS)"
                    asc = 1
                elif ans5 == 4:
                    course_opting_for = "BSc(PME)"
                    asc = 1
                else:
                    print("\nEnter a valid option")

        elif stream_opting_for == "Commerce":
            aco = 0
            while(aco == 0):  
                ans5 = int(input("\nSelect the course your opting for : \n1. BBA\n2. BBA in Aviation\n3. BCom\n4. BCom in Finance\n5. BCom in Tourism\nEnter option number : "))  
                if ans5 == 1:
                    course_opting_for = "BBA"
                    aco = 1
                elif ans5 == 2:
                    course_opting_for = "BBA in Aviation"
                    aco = 1
                elif ans5 == 3:
                    course_opting_for = "BCom"
                    coa = 1
                elif ans5 == 4:
                    course_opting_for = "BCom in Finance"
                    aco = 1
                elif ans5 == 5:
                    course_opting_for = "BCom in Tourism"
                    aco = 1
                else:
                    print("Enter a valid option")
        
        elif stream_opting_for == "Arts":
            aar = 0
            while(aar == 0): 
                ans5 = int(input("\nSelect the course your opting for : \n1. BA in Sociology\n2. BA in Economics\n3. BA in English\nEnter option number : "))
                if ans5 == 1:
                    course_opting_for = "BA in Sociology"
                    aar = 1
                elif ans5 == 2:
                    course_opting_for = "BA in Economics"
                    aar = 1
                elif ans5 == 3:
                    course_opting_for = "BA in English"
                    aar = 1
                else:
                    print("\nEnter a valid option")
        
        achievements = input("\nEnter any achievements achieved : ")  
        a = Admission(fname, lname, gender, dob, phoneno, emailid, address, father_name, father_occupation, mother_name, mother_occupation, category, tenth_score, twelveth_score, previous_stream, stream_opting_for, course_opting_for, achievements)
        print(f"\nThank you for applying. Your application number is {a.get_app_no()} \nPlease wait as we process your application and check your eligibility for the chosen course.\n")
        selection_process(a)
        admission()

    def selection_process(a):
        message = ""
        # Importing methods from Admission class
        # Checking course availability
        if Admission.check_course_availability(a) == True:
            # Checking eligibility
            if Admission.check_eligibility(a) == True:
                a.set_status("Admitted")
            else:
                a.set_status("Not admitted")
                message = Admission.check_eligibility(a)
                
            # Getting all the info in a dictionary.
            old_info = a.__dict__
            new_info = {}
            for i, j in old_info.items():
                key = i.replace("_Admission__","")
                new_info[key] = j
                data = [new_info]

            # Writing the info dictionary to a csv file.
            fields = ["appno","first_name","last_name","gender","dob","phone_no","email_id","address","father_name","father_occupation","mother_name","mother_occupation","category","tenth_score","twelveth_score","previous_stream","stream_opting_for","course_opting_for","achievements","status","documents"]
            with open('database.csv','a',newline='') as f:
                writer = csv.DictWriter(f,fieldnames = fields)
                writer.writerows(data)
            
            return message

        else:
            message = Admission.check_course_availability(a)
            return message

    clear()
    print(" Admissions Department ".center(146, '-')+"\n")
    print("Welcome to the Admissions Department.".center(150))
    print("Please select an option to proceed.\n\n1. Apply\n2. Update your application\n3. Review your application\n4. Go back")
    ans = int(input("\nEnter the option number : "))

    def update_app():
        clear()
        print(" Update Application ".center(146,'-'))
        print("\nPress 0 to go back to main menu")
        appno = input("\nEnter your application number : ")
        if int(appno) == 0:
            admission()
        csv_file_reader = csv.reader(open("C:\\Users\\2145644\\OOPS Project\\database.csv","r"))
        columns = ["Application No.","First name","Last name","Gender","DOB","Phone Number","Email-ID","Address","Father name","Father occupation","Mother name","Mother occupation","Category","10th score","12th score","Previous stream","Opting stream","Opting course","Achievements","Documents"]
        index = 0
        row_pos = 0
        for row in csv_file_reader:
            if row[0] == appno:
                for i in range(len(row)):
                    if index == 19:
                        continue
                    print(f"\n{index} . {columns[index]} : {row[index]}")
                    index += 1
                break
            else:
                row_pos += 1

        counter = 0
        df = pd.read_csv("database.csv")
        while(counter == 0):
            option = int(input("\nEnter the option number to change : "))
            if option == 1:
                u_fname = input("\nEnter your first name : ")
                df.loc[(row_pos - 1), 'first_name'] = u_fname

            elif option == 2:
                u_lname = input("\nEnter your last name : ")
                df.loc[(row_pos - 1), 'last_name'] = u_lname
            
            elif option == 3:
                ans1 = int(
                input("\nEnter your gender \n1. Male \n2. Female\nEnter the option number : "))
                if ans1 == 1:
                    u_gender = "Male"
                else:
                    u_gender = "Female"
                df.loc[(row_pos - 1), 'gender'] = u_gender
            
            elif option == 4:
                u_dob = input("\nEnter your DOB in DD/MM/YYYY format : ")
                condition = True
                while (condition):
                    p = r"\d{2}/\d{2}/\d{4}"
                    result = re.findall(p, u_dob)
                    if len(result) > 0:
                        break
                    else:
                        print("\nInvalid format !")
                        
                df.loc[(row_pos - 1), 'dob'] = u_dob
            
            elif option == 5:
                u_phoneno = input("\nEnter your Phone No. : ")
                while (len(u_phoneno) != 10 or u_phoneno.isdigit() == False):
                    print("\nEnter a valid phome number")
                    u_phoneno = input("\nEnter your Phone No. : ")
                df.loc[(row_pos - 1), 'phone_no'] = u_phoneno
            
            elif option == 6:
                u_emailid = input("\nEnter your Email-ID: ")
                while (u_emailid.endswith(".com") == False or "@" not in u_emailid):
                    print("\nPlease enter a valid Email-ID")
                    u_emailid = input("\nEnter your Email-ID : ")
                df.loc[(row_pos - 1), 'email_id'] = u_emailid
            
            elif option == 7:
                u_address = input("\nEnter your address : ")
                df.loc[(row_pos - 1), 'address'] = u_address
            
            elif option == 8:
                u_fathername = input("\nEnter your Father's name : ")
                df.loc[(row_pos - 1), 'father_name'] = u_fathername
            
            elif option == 9:
                u_fatheroccupation = input("\nEnter your Father's occupation: ")
                df.loc[(row_pos - 1), 'father_occupation'] = u_fatheroccupation
            
            elif option == 10:
                u_mothername = input("\nEnter your Mother's name : ")
                df.loc[(row_pos - 1), 'mother_name'] = u_mothername
            
            elif option == 11:
                u_motheroccupation = input("\nEnter your Mother's occupation: ")
                df.loc[(row_pos - 1), 'mother_occupation'] = u_motheroccupation
            
            elif option == 12:
                a = 0
                while(a == 0):  
                    ans2 = int(input(
                        "\nSelect your Category \n1. General\n2. SC|ST\n3. 2B\n4. 3B\nEnter option number :  "))
                    if ans2 == 1:
                        u_category = "General"
                        a = 1
                    elif ans2 == 2:
                        u_category = "SC|ST"
                        a = 1
                    elif ans2 == 3:
                        u_category = "2B"
                        a = 1
                    elif ans2 == 4:
                        u_category = "3B"
                        a = 1
                    else:
                        print("\nEnter a valid option number")
                        
                df.loc[(row_pos - 1), 'category'] = u_category

            elif option == 13:
                u_tenth = input("\nEnter your 10th grade marks : ")
                df.loc[(row_pos - 1), 'tenth_score'] = u_tenth
            
            elif option == 14:
                u_twelve = input("\nEnter your 12th grade marks : ")
                df.loc[(row_pos - 1), 'twelveth_score'] = u_twelve
            
            elif option == 15:
                a = 0
                while(a == 0): 
                    ans3 = int(input("\nSelect your previous stream \n1. Science\n2. Commerce\n3. Arts\nEnter option number : "))
                    if ans3 == 1:
                        u_previous_stream = "Science"
                        a = 1
                    elif ans3 == 2:
                        u_previous_stream = "Commerce"
                        a = 1
                    elif ans3 == 3:
                        u_previous_stream = "Arts"
                        a = 1
                    else:
                        print("\nEnter a valid option")
                df.loc[(row_pos - 1), 'previous_stream'] = u_previous_stream

            elif option == 16:
                a = 0
                while(a == 0): 
                    ans4 = int(input("\nSelect the stream you want to opt for \n1. Science\n2. Commerce\n3. Arts\nEnter option number : "))
                    if ans4 == 1:
                        u_stream_opting_for = "Science"
                        a = 1
                    elif ans4 == 2:
                        u_stream_opting_for = "Commerce"
                        a = 1
                    elif ans4 == 3:
                        u_stream_opting_for = "Arts"
                        a = 1
                    else:
                        print("\nEnter a valid option")
                       
                df.loc[(row_pos - 1), 'stream_opting_for'] = u_stream_opting_for

            elif option == 17:
                if u_stream_opting_for == "Science":
                    a = 0
                    while(a == 0):     
                        ans5 = int(input("\nSelect the course your opting for : \n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\nEnter option number : "))
                        if ans5 == 1:
                            u_course_opting_for = "BCA"
                            a = 1
                        elif ans5 == 2:
                            u_course_opting_for = "BCA in Analytics"
                            a = 1
                        elif ans5 == 3:
                            u_course_opting_for = "BSc(PMCS)"
                            a = 1
                        elif ans5 == 4:
                            u_course_opting_for = "BSc(PME)"
                            a = 1
                        else:
                            print("\nEnter a valid option")
                            
                elif u_stream_opting_for == "Commerce":
                    a = 0
                    while(a == 0):  
                        ans5 = int(input("\nSelect the course your opting for : \n1. BBA\n2. BBA in Aviation\n3. BCom\n4. BCom in Finance\n5. BCom in Tourism\nEnter option number : "))  
                        if ans5 == 1:
                            u_course_opting_for = "BBA"
                            a = 1
                        elif ans5 == 2:
                            u_course_opting_for = "BBA in Aviation"
                            a = 1
                        elif ans5 == 3:
                            u_course_opting_for = "BCom"
                            a = 1
                        elif ans5 == 4:
                            u_course_opting_for = "BCom in Finance"
                            a = 1
                        elif ans5 == 5:
                            u_course_opting_for = "BCom in Tourism"
                            a = 1
                        else:
                            print("Enter a valid option")
        
                elif u_stream_opting_for == "Arts":
                    a = 0
                    while(a == 0): 
                        ans5 = int(input("\nSelect the course your opting for : \n1. BA in Sociology\n2. BA in Economics\n3. BA in English\nEnter option number : "))
                        if ans5 == 1:
                            u_course_opting_for = "BA in Sociology"
                            a = 1
                        elif ans5 == 2:
                            u_course_opting_for = "BA in Economics"
                            a = 1
                        elif ans5 == 3:
                            u_course_opting_for = "BA in English"
                            a = 1
                        else:
                            print("\nEnter a valid option")
                df.loc[(row_pos - 1), 'course_opting_for'] = u_course_opting_for

            elif option == 18:
                u_achievements = input("\nEnter your achievements : ")
                df.loc[(row_pos - 1), 'achievements'] = u_achievements
            
            df.to_csv("database.csv", index=False)

            if option == 0:
                counter = 1
                admission()

    if ans == 1:
        apply()
    elif ans == 2:
        update_app()
    elif ans == 3:
        review()
    elif ans == 4:
        main_menu()


main_menu()
