print("""                                                           ==============**************=================
                                                                    WELCOME TO LOAN MANAGEMENT SYSTEM
                                                           ==============**************=================                                                        """)

print("You should create a database sravan to go ahead ")
import mysql.connector as sqltor

Mycon = sqltor.connect(host="localhost", user="root", passwd="9797211121", database="sravan",auth_plugin='mysql_native_password')
cursor = Mycon.cursor(buffered=True)

cursor.execute(""" CREATE TABLE IF NOT EXISTS LOAN(LoanId integer PRIMARY KEY,Name varchar(60),Age integer,
                   Phonenumber integer,Loantype varchar(20),
                   AadhaarCardNumber integer,JobName char(60),AnnualSalary integer,LoanAmount integer,
                   PermanentAddress varchar(100), LoanTenure_years integer,BalanceAmount float)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS CARLOAN(CarLoanId integer PRIMARY KEY,Name varchar(60),
                    Age integer,AadhaarCardNumber integer,
                  MobileNumber integer,JobName varchar(40),AnnualSalary integer,CarName varchar(40),
                  CarPrice integer,BalanceAmount float)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS HOMELOAN(HomeLoanId integer PRIMARY KEY,Name varchar(60),
                   Age integer,AadhaarCardNumber integer,
                  MobileNumber integer,JobName varchar(40),AnnualSalary integer,HomePlace varchar(60),
                  HomePrice integer,BalanceAmount float)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS EDUCATIONALLOAN(EducationalLoanId integer PRIMARY KEY,
                  Name varchar(60),Age integer,AadhaarCardNumber integer,
                    MobileNumber integer,College varchar(60),Studying integer,BalanceAmount float)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS BUSINESSLOAN(BusinessLoanId integer PRIMARY KEY,Name varchar(60),
                   Age integer,AadhaarCardNumber integer,
                    MobileNumber integer ,BusinessName varchar(40),AnnualSalary integer,BalanceAmount float)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS PERSONELLOAN(PersonelLoanId integer  PRIMARY KEY,Name varchar(60),
                   Age integer,AadhaarCardNumber integer,
                    MobileNumber integer,ReasonForLoan varchar(100),AnnualSalary integer,BalanceAmount float)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS  GOLDLOAN(GoldLoanId integer PRIMARY KEY,Name varchar(60),Age integer,
                    AadhaarCardNumber integer,MobileNumber integer,
                    AnnualSalary integer,Weight integer,BalanceAmount float)""")


def conversion(x):
    tupple = x[0]
    string = tupple[0]
    return string


def remainingamount(u):
    cursor.execute("""SELECT    BalanceAmount
                        FROM LOAN
                        WHERE LoanId={}""".format(u))
    r = cursor.fetchall()
    x = conversion(r)
    return x


def balance(r, months, n):
    t = r + (r * months * n) // 1200
    return t


def left(b, paying):
    k = b - paying
    f = int(k)
    return f


def up(left, u):
    query = """ UPDATE LOAN
                     SET BalanceAmount=%s
                     WHERE LoanId like %s"""
    values = (left, u)
    cursor.execute(query, values)
    Mycon.commit()


def idetails(ids):
    cursor.execute("""SELECT *
                      FROM LOAN
                      WHERE LoanId like {}""".format(ids))
    a = cursor.fetchall()
    print(a)


while True:
    n = int(input("""Choose an option:
            1.Want to take loan
            2.Want to pay loan
            3.Want to check balance amount to be paid
            4.Want to pay all amount
            5.Want to see all details of customers(This is only for our company officials for official purpose)
            6.EXIT
            PRESS CORRESPONDING NUMBER ONLY WITHOUT DOT
            :"""))
    print("==============================================================================")
    if n == 1:
        k = int(input("""What type of loan you want to take:
                    1.Car Loan
                    2.Home Loan
                    3.Educational Loan
                    4.Business Loan
                    5.Personal Loan
                    6.Gold Loan
                    PRESS CORRESPONDING NUMBER ONLY WITHOUT DOT
                    :"""))
        print("===========================================================================")
        if k == 1:
            print("""The Details and requirements  of your selected Car loan are as follows:
                  1.Your age should be 21-65yrs
                  2.Your annual income should be atleast 3 lakhs
                  3.You should be user of our bank
                  4.You can take maximum tenure 7years
                  5.This information should be given to the asked authority :
                    Filled up loan application form,Passport Size photo,PhotCopy of Income Tax ,PANIdentity,Proof
                    –Aadhaar,PasspoDriving License ,Voter ID, PANQuotation of carResidential, Address Proof, License,
                    Registered Rent Agreement, Utility Bill (upto 3 months old), PassporIncome Documents – 3 months pay
                    slip,2 years Form 16,3 months bank statement showing salary credit and any EMI debit ,
                    R.C of Vehicle and Insurance of Car
                  6.The interest rate would be 8%
                    FOR FURTHER DETAILS CONTACT OUR BRANCH MANAGER """)
            conf = int(input("So do you want to  continue ,press 1 to continue or press 2 to discontinue:"))
            if conf == 1:
                print("Now you have to enter your details")
                carloanid = int(input("Enter unique CarLoanId (Should be entered through our officicals):"))
                loanid = int(input("Enter unique LoanId (Should be entered through our officicals):"))
                name = input("Enter your name :")
                age = int(input("Enter your age :"))
                aadhaarcardnumber = int(input("Enter Aadhaar card number:"))
                mobilenumber = int(input("Enter your mobile number:"))
                job = input("Enter your job name:")
                salary = int(input("Enter your annual salary:"))
                carname = input("Enter your car name with brand :")
                carprice = int(input("Enter price of your car(without commas):"))
                loanamount = int(input("Enter loan amount you are going to take :"))
                loantype = "CAR LOAN"
                address = input("Enter your permanent address:")
                cursor.execute("""INSERT INTO CARLOAN(CarLoanId,Name,Age,AadhaarCardNumber,MobileNumber,JobName,
                                  AnnualSalary, CarName,CarPrice,BalanceAmount)
                                VALUES({},'{}',{},{},{},'{}',{},'{}',{},{}) """.format(carloanid, name, age,
                                                                                       aadhaarcardnumber, mobilenumber,
                                                                                       job, salary, carname, carprice,
                                                                                       loanamount))
                Mycon.commit()
                cursor.execute(""" INSERT INTO LOAN(LoanId,Name,Age,PhoneNumber,Loantype,AadhaarCardNumber,
             JobName,AnnualSalary,LoanAmount,PermanentAddress,LoanTenure_years,BalanceAmount)
                                    VALUES({},'{}',{},{},'{}',{},'{}',{},{},'{}',{},{})""".format(loanid, name, age,
                                                                                                  mobilenumber,
                                                                                                  loantype,
                                                                                                  aadhaarcardnumber,
                                                                                                  job, salary,
                                                                                                  loanamount, address,
                                                                                                  7, loanamount))
                Mycon.commit()
                print("You should remember your loan id.Its very important")
                print(" Thank You for taking loan from our bank. We will meet you soon")
                print("=============================================================")
                continue
            else:
                print("Thank You")
                print("==============================================================")
                continue
        elif k == 2:
            print("""The Details and requirements  of your selected Home loan are as follows:
                    1.Your age should be 21-65yrs
                    2.Your annual income should be atleast 3 lakhs
                    3.you should be user of our bank
                    4.you can take maximum tenure 20years
                    5.This information should be given to the asked authority :
                      *Completed Home Loan Application Form.
                      *Passport size Photographs.
                      *Proof of Identification: like PAN Card. ...
                      *Proof of Age: like Aadhaar Card. ...
                      *Proof of Residence: 
                      *Income Documents: 
                      *Property Documents Required For Home Loan:
                    6.The interest rate would be 7.5%
                    FOR FURTHER DETAILS CONTACT OUR BRANCH MANAGER""")
            conf = int(input("So do you want to  continue ,press 1 to continue or press 2 to discontinue:"))
            if conf == 1:
                print("Now you have to enter your details")
                homeloanid = int(input("Enter unique HomeLoanId (Should be entered through our officicals):"))
                loanid = int(input("Enter unique LoanId (Should be entered through our officicals):"))
                name = input("Enter your name :")
                age = int(input("Enter your age :"))
                aadhaarcardnumber = int(input("Enter Aadhaar card number:"))
                mobilenumber = int(input("Enter your mobile number:"))
                job = input("Enter your job name:")
                salary = int(input("Enter your annual salary:"))
                place = input("Enter your house constructing area")
                homeprice = int(input("Enter price of your home:"))
                loanamount = int(input("Enter loan amount you are going to take :"))
                loantype = "HOME LOAN"
                address = input("Enter your permanent address:")
                cursor.execute("""INSERT INTO HOMELOAN(HomeLoanId,Name,Age,AadhaarCardNumber,MobileNumber,
                                    JobName,AnnualSalary,HomePlace,HomePrice,BalanceAmount)
                                    VALUES({},'{}',{},{},{},'{}',{},'{}',{},{}) """.format(homeloanid, name, age,
                                                                                           aadhaarcardnumber,
                                                                                           mobilenumber, job, salary,
                                                                                           place, homeprice,
                                                                                           loanamount))
                Mycon.commit()
                cursor.execute(""" INSERT INTO LOAN(LoanId,Name,Age,PhoneNumber,Loantype,AadhaarCardNumber,
                                   JobName,AnnualSalary,LoanAmount,PermanentAddress,LoanTenure_years,BalanceAmount)
                                    VALUES({},'{}',{},{},'{}',{},'{}',{},{},'{}',{},{})""".format(loanid, name, age,
                                                                                                  mobilenumber,
                                                                                                  loantype,
                                                                                                  aadhaarcardnumber,
                                                                                                  job, salary,
                                                                                                  loanamount, address,
                                                                                                  20, loanamount))
                Mycon.commit()
                print("You should remember your loan id.Its very important")
                print(" Thank You for taking loan from our bank. We will meet you soon")
                print("========================================================")
                continue
            else:
                print("Thank You")
                print("==========================================================")
                continue
        elif k == 3:
            print("""The Details and requirements  of your selected home loan are as follows:
                    1.Your age should be 10-20yrs
                    2.Your annual income should be atleast 3 lakhs
                    3.you should be user of our bank
                    4.you can take maximum tenure 4years
                    5.This information should be given to the asked authority :
                      *Duly-filled application form.
                      *2 passport size photographs.
                      *Graduation, Secondary School Certificate, or High School Certificate or mark sheets.
                      *KYC documents that include ID, address, and age proof.
                      *Signature Proof.
                      *Income Proof of parents or guardian.
                    6.The interest rate would be 9.5%
                    FOR FURTHER DETAILS CONTACT OUR BRANCH MANAGER""")
            conf = int(input("So do you want to  continue ,press 1 to continue or press 2 to discontinue:"))
            if conf == 1:
                print("Now you have to enter your details")
                educationalloanid = int(
                    input("Enter unique Educational LoanId (Should be entered through our officicals):"))
                loanid = int(input("Enter unique LoanId (Should be entered through our officicals):"))
                name = input("Enter your name :")
                age = int(input("Enter your age :"))
                aadhaarcardnumber = int(input("Enter Aadhaar card number:"))
                mobilenumber = int(input("Enter your mobile number:"))
                college = input("Enter your school/college name:")
                studying = int(input("Enter your class numerically:"))
                loanamount = int(input("Enter loan amount you are going to take :"))
                loantype = "EDUCATIONAL LOAN"
                job = "NA"
                salary = 0
                address = input("Enter your permanent address:")
                cursor.execute("""INSERT INTO EDUCATIONALLOAN(EducationalLoanId,Name,Age,AadhaarCardNumber,
                                    MobileNumber,College,Studying,BalanceAmount)
                                    VALUES({},'{}',{},{},{},'{}',{},{}) """.format(educationalloanid, name, age,
                                                                                   aadhaarcardnumber, mobilenumber,
                                                                                   college, studying, loanamount))
                Mycon.commit()
                cursor.execute(""" INSERT INTO LOAN(LoanId,Name,Age,PhoneNumber,Loantype,AadhaarCardNumber,JobName,AnnualSalary,
                                    LoanAmount,PermanentAddress,LoanTenure_years,BalanceAmount)
                                    VALUES({},'{}',{},{},'{}',{},'{}',{},{},'{}',{},{})""".format(loanid, name, age,
                                                                                                  mobilenumber,
                                                                                                  loantype,
                                                                                                  aadhaarcardnumber,
                                                                                                  job, salary,
                                                                                                  loanamount, address,
                                                                                                  4, loanamount))
                Mycon.commit()
                print("You should remember your loan id.Its very important")
                print(" Thank You for taking loan from our bank. We will meet you soon")
                print("========================================================")
                continue
            else:
                print("Thank You")
                print("==========================================================")
                continue
        elif k == 4:
            print("""The Details and requirements  of your selected business loan are as follows:
                    1.Passport sized photographs
                    2.Valid Aadhaar card, Voter ID or Passport.
                    3.Bank Statements
                    4.Certified bank statements of the borrower for the past 6 months
                    5.Proof of Business
                    6.Trade license or sales tax certificate
                    7.Ownership documents
                    8.Sole proprietorship or partnership deed
                    9.Income tax returns for the past 2 financial years
                    10.Profit and loss statements for the past 2 financial years
                    11.Balance sheets from previous years
                    12.The interest rate would be 13%
                    13.Maximum loan tenure is 15 years
                    FOR FURTHER DETAILS CONTACT OUR BRANCH MANAGER""")
            conf = int(input("So do you want to  continue ,press 1 to continue or press 2 to discontinue:"))
            if conf == 1:
                print("Now you have to enter your details")
                businessloanid = int(input("Enter unique BusinessLoanId (Should be entered through our officicals):"))
                loanid = int(input("Enter unique LoanId (Should be entered through our officicals):"))
                name = input("Enter your name :")
                age = int(input("Enter your age :"))
                aadhaarcardnumber = int(input("Enter Aadhaar card number:"))
                mobilenumber = int(input("Enter your mobile number:"))
                businessname = input("Enter your business name:")
                annualincome = int(input("Enter expected annual income came from this business:"))
                loanamount = int(input("Enter loan amount you are going to take :"))
                loantype = "BUSINESS LOAN"
                job = input("Enter your current job.If there is no current job enter NILL:")
                salary = int(input("Enter your current salary.If there is no current salary enter NILL:"))
                address = input("Enter your current address:")
                cursor.execute("""INSERT INTO BUSINESSLOAN(BusinessLoanId,Name,Age,AadhaarCardNumber,MobileNumber,
                                    BusinessName,AnnualSalary,BalanceAmount)
                                    VALUES({},'{}',{},{},{},'{}',{},{}) """.format(businessloanid, name, age,
                                                                                   aadhaarcardnumber, mobilenumber,
                                                                                   businessname, annualincome,
                                                                                   loanamount))
                Mycon.commit()
                cursor.execute(""" INSERT INTO LOAN(LoanId,Name,Age,PhoneNumber,Loantype,AadhaarCardNumber,
                                     JobName,AnnualSalary,LoanAmount,PermanentAddress,LoanTenure_years,BalanceAmount)
                                    VALUES({},'{}',{},{},'{}',{},'{}',{},{},'{}',{},{})""".format(loanid, name, age,
                                                                                                  mobilenumber,
                                                                                                  loantype,
                                                                                                  aadhaarcardnumber,
                                                                                                  job, salary,
                                                                                                  loanamount, address,
                                                                                                  15, loanamount))
                Mycon.commit()
                print("You should remember your loan id.Its very important")
                print(" Thank You for taking loan from our bank. We will meet you soon")
                print("================================================================")
                continue

            else:
                print("Thank You")
                print("=================================================================")
                continue
        elif k == 5:
            print("""The Details and requirements  of your selected personel loan are as follows:

              1.Proof of Identity:- Passport / Driving License / Voters ID / PAN Card (any one)
              2.Proof of Residence:- Leave and License Agreement / Utility Bill (not more than 3 months old) /
              Passport (any one).
              3.Latest 3 months Bank Statement (where salary/income is credited).
              4.Salary slips for last 3 months.
              5.Interest would be 11%
              6.The maximum loan tenure is 7 years
              FOR FURTHER DETAILS CONTACT OUR BRANCH MANAGER""")
            conf = int(input("So do you want to  continue ,press 1 to continue or press 2 to discontinue:"))
            if conf == 1:
                print("Now you have to enter your details")
                personelloanid = int(input("Enter unique PersonelLoanId (Should be entered through our officicals):"))
                loanid = int(input("Enter unique LoanId (Should be entered through our officicals):"))
                name = input("Enter your name :")
                age = int(input("Enter your age :"))
                aadhaarcardnumber = int(input("Enter Aadhaar card number:"))
                mobilenumber = int(input("Enter your mobile number:"))
                reasonforloan = input("Enter reason for taking loan:")
                salary = int(input("Enter your annual income:"))
                loanamount = int(input("Enter loan amount you are going to take :"))
                job = input("Enter your current job:")
                loantype = "PERSONEL LOAN"
                address = input("Enter your current address:")
                cursor.execute("""INSERT INTO PERSONELLOAN(PersonelLoanId,Name,Age,AadhaarCardNumber,MobileNumber,
                                    ReasonForLoan,AnnualSalary,BalanceAmount)
                                    VALUES({},'{}',{},{},{},'{}',{},{})""".format(personelloanid, name, age,
                                                                                  aadhaarcardnumber, mobilenumber,
                                                                                  reasonforloan, salary, loanamount))
                Mycon.commit()
                cursor.execute(""" INSERT INTO LOAN(LoanId,Name,Age,PhoneNumber,Loantype,AadhaarCardNumber,
                                     JobName,AnnualSalary,LoanAmount,PermanentAddress,LoanTenure_years,BalanceAmount)
                                    VALUES({},'{}',{},{},'{}',{},'{}',{},{},'{}',{},{})""".format(loanid, name, age,
                                                                                                  mobilenumber,
                                                                                                  loantype,
                                                                                                  aadhaarcardnumber,
                                                                                                  job, salary,
                                                                                                  loanamount, address,
                                                                                                  7, loanamount))
                Mycon.commit()
                print("You should remember your loan id.Its very important")
                print(" Thank You for taking loan from our bank. We will meet you soon")
                print("======================================================================")
                continue
            else:
                print("Thank You")
                print("=====================================================================")
                continue
        else:
            print("""The Details and requirements  of your selected Gold loan are as follows:
                    1.Your age should be 21-65yrs
                    2.Your annual income should be atleast 1 lakh
                    3.you should be user of our bank
                    4.you can take maximum tenure 20years
                    5.This information should be given to the asked authority :
                      *Aadhar Card
                      *PAN Card
                      *Valid Driving License(for address proof)
                      *Valid Passport
                      *Voter’s ID Card
                      *Job Card issued by NREGA
                    6.The intrest rate would be 1%
                    7. The maximum loan tenure is 1 year
                    FOR FURTHER DETAILS CONTACT OUR BRANCH MANAGER""")
            conf = int(input("So do you want to  continue ,press 1 to continue or press 2 to discontinue:"))
            if conf == 1:
                print("Now you have to enter your details")
                goldloanid = int(input("Enter unique GoldLoanId (Should be entered through our officicals):"))
                loanid = int(input("Enter unique LoanId (Should be entered through our officicals):"))
                name = input("Enter your name :")
                age = int(input("Enter your age :"))
                aadhaarcardnumber = int(input("Enter Aadhaar card number:"))
                mobilenumber = int(input("Enter your mobile number:"))
                annualincome = int(input("Enter your annual income:"))
                weight = int(input("Enter weight of your gold in grams:"))
                loanamount = weight * 3000
                loantype = "GOLD LOAN"
                job = input("Enter your current job:")
                salary = int(input("Enter your current salary:"))
                address = input("Enter your permanent address:")
                print("The amount that you get for the given weight of loan is", loanamount)
                cursor.execute("""INSERT INTO GOLDLOAN(GoldLoanId,Name,Age,AadhaarCardNumber,MobileNumber,
                                    AnnualSalary,Weight,BalanceAmount)
                                    VALUES({},'{}',{},{},{},{},{},{})""".format(goldloanid, name, age,
                                                                                aadhaarcardnumber,
                                                                                mobilenumber, annualincome, weight,
                                                                                loanamount))
                Mycon.commit()
                cursor.execute(""" INSERT INTO LOAN(LoanId,Name,Age,PhoneNumber,Loantype,AadhaarCardNumber,JobName,
                                     AnnualSalary,LoanAmount,PermanentAddress,LoanTenure_years,BalanceAmount)
                                    VALUES({},'{}',{},{},'{}',{},'{}',{},{},'{}',{},{})""".format(loanid, name, age,
                                                                                                  mobilenumber,
                                                                                                  loantype,
                                                                                                  aadhaarcardnumber,
                                                                                                  job, salary,
                                                                                                  loanamount, address,
                                                                                                  1, loanamount))

                Mycon.commit()
                print("You should remember your loan id.Its very important")
                print(" Thank You for taking loan from our bank. We will meet you soon")
                print("==================================================================")
                continue
            else:
                print("Thank You")
                print("=================================================================")
                continue

    elif n == 2:
        print("So you want to repay loan amount,Make sure you filled all details during taking loan:")
        loantype = int(input("""Which type of loan you have taken:
                          1.Car Loan
                          2.Home Loan
                          3.Educational Loan
                          4.Business Loan
                          5.Personal Loan
                          6.Gold Loan
                            PRESS CORRESPONDING NUMBER ONLY WITHOUT DOT
                            :"""))
        print("===================================================================")
        if loantype == 1:
            print("So you have taken car loan")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your CarLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 8
            b = balance(r, months, n)
            print("The remaing amount that you have to pay is:", b)
            paying = int(input("The amount that you want to pay is:"))

            l = left(b, paying)

            print("Now you left with the amount that have to pay is", l)
            up(l, u)
            cursor.execute(""" UPDATE CARLOAN
                      SET BalanceAmount={}
                      WHERE CarLoanId like {}""".format(l, c))
            print("Thank you . Meet you again")
            print("================================================================")
            continue
        elif loantype == 2:
            print("So you have taken Home loan:")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your HomeLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 7.5
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            paying = int(input("The amount that you want to pay is:"))

            l = left(b, paying)
            print("Now you left with the amount that have to pay is", l)
            up(l, u)
            cursor.execute(""" UPDATE HOMELOAN
                      SET BalanceAmount={}
                      WHERE HomeLoanId like {}""".format(l, c))
            Mycon.commit()
            print("Thank you . Meet you again")
            print("=====================================================================")
            continue
        elif loantype == 3:
            print("So you have taken Educational loan:")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your EducationalLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 9.5
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            paying = int(input("The amount that you want to pay is:"))

            l = left(b, paying)
            print("Now you left with the amount that have to pay is", l)
            up(l, u)
            cursor.execute(""" UPDATE EDUCATIONALLOAN
                      SET BalanceAmount={}
                      WHERE EducationalLoanId like {}""".format(l, c))
            Mycon.commit()
            print("Thank you . Meet you again")
            print("================================================================")
            continue
        elif loantype == 4:
            print("So you have taken Business loan:")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your BusinessLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 13
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            paying = int(input("The amount that you want to pay is:"))

            l = left(b, paying)
            print("Now you left with the amount that have to pay is", l)
            up(l, u)
            cursor.execute(""" UPDATE BUSINESSLOAN
                      SET BalanceAmount={}
                      WHERE BusinessLoanId like {}""".format(l, c))
            print("Thank you . Meet you again")
            print("===================================================================")
            continue
        elif loantype == 5:
            print("So you have taken Personel loan:")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your PersonelLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 11
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            paying = int(input("The amount that you want to pay is:"))

            l = left(b, paying)
            print("Now you left with the amount that have to pay is", l)
            up(l, u)
            cursor.execute(""" UPDATE PERSONELLOAN
                      SET BalanceAmount={}
                      WHERE PersonelLoanId like {}""".format(l, c))
            print("Thank you . Meet you again")
            print("=========================================================")
            continue
        elif loantype == 6:
            print("So you have taken Gold loan:")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your GoldLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 1
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            paying = int(input("The amount that you want to pay is:"))

            l = left(b, paying)
            print("Now you left with the amount that have to pay is", l)
            up(l, u)
            cursor.execute(""" UPDATE GOLDLOAN
                      SET BalanceAmount={}
                      WHERE GoldLoanId like {}""".format(l, c))
            print("Thank you . Meet you again")
            print("======================================================================")
            continue
        else:
            print("You enterd a wrong choice, please re-enter")
            continue
    elif n == 3:
        print("So you want to check loan amount,Make sure you filled all details during taking loan:")
        loantype = int(input("""Which type of loan you have taken:
                          1.Car Loan
                          2.Home Loan
                          3.Educational Loan
                          4.Business Loan
                          5.Personal Loan
                          6.Gold Loan
                            PRESS CORRESPONDING NUMBER ONLY WITHOUT DOT
                            :"""))
        print("=========================================================================")
        if loantype == 1:
            print("So you have taken car loan:")
            u = int(input("Enter your LoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 8
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            print("Thank you . Meet you again")
            print("===========================================================")
            continue
        elif loantype == 2:
            print("So you have taken Home loan:")
            u = int(input("Enter your LoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 7.5
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            print("Thank you . Meet you again")
            print("==================================================================")
            continue
        elif loantype == 3:
            print("So you have taken Educational loan:")
            u = int(input("Enter your LoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 9.5
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            print("Thank you . Meet you again")
            print("====================================================================")
            continue
        elif loantype == 4:
            print("So you have taken Business loan:")
            u = int(input("Enter your LoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 13
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            print("Thank you . Meet you again")
            print("=========================================================")
            continue
        elif loantype == 5:
            print("So you have taken Personel loan:")
            u = int(input("Enter your LoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 11
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            print("Thank you . Meet you again")
            print("=================================================================")
            continue
        else:
            print("So you have taken Gold loan:")
            user = int(input("Enter your LoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 1
            b = balance(r, months, n)

            print("the remaing amount that you have to pay is:", b)
            print("Thank you . Meet you again")
            print("=============================================================")
            continue
    elif n == 4:
        print("So you want to repay all amount:")
        loantype = int(input("""Which type of loan you have taken:
                          1.Car Loan
                          2.Home Loan
                          3.Educational Loan
                          4.Business Loan
                          5.Personal Loan
                          6.Gold Loan
                            PRESS CORRESPONDING NUMBER ONLY WITHOUT DOT
                            :"""))
        print("================================================================")
        if loantype == 1:
            print("So you have taken Car loan")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your CarLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 8
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            t = input("So you have paid all amount.Yes or No:")
            if t == "Yes":
                print("Thank you for paying.Hope that we will meet you again")
                cursor.execute("""DELETE
                      FROM CARLOAN
                      WHERE CarloanId like {}""".format(c))
                Mycon.commit()
                print("===============================================================")
                continue
            else:
                print("Hope that you will pay soon.Thank You")
                print("================================================================")
                continue
        elif loantype == 2:
            print("So you have taken home loan")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your HomeLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 7.5
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            t = input("So you have paid all amount.Yes or No:")
            if t == "Yes":
                print("Thank you for paying.Hope that we will meet you again")
                cursor.execute("""DELETE
                      FROM HOMELOAN
                      WHERE homeLoanId like {}""".format(c))
                Mycon.commit()
                print("=======================================================")
                continue
            else:
                print("Hope that you will pay soon.Thank You")
                print("=============================================================")
                continue
        elif loantype == 3:
            print("So you have taken Educational loan")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your EducationalLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 9.5
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            t = input("So you have paid all amount.Yes or No:")
            if t == "Yes":
                print("Thank you for paying.Hope that we will meet you again")
                cursor.execute("""DELETE
                      FROM EDUCATIONALLOAN
                      WHERE educationalLoanId like {}""".format(c))
                Mycon.commit()
                print("==========================================================")
                continue
            else:
                print("Hope that you will pay soon.Thank You")
                print("===========================================================")
                continue
        elif loantype == 4:
            print("So you have taken Business loan")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your BusinessLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 13
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            t = input("So you have paid all amount.Yes or No:")
            if t == "Yes":
                print("Thank you for paying.Hope that we will meet you again")
                cursor.execute("""DELETE
                      FROM BUSINESSLOAN
                      WHERE businessLoanId like {}""".format(c))
                Mycon.commit()
                print("============================================================")
                continue
            else:
                print("Hope that you will pay soon.Thank You")
                print("==============================================================")
                continue
        elif loantype == 5:
            print("So you have taken personel loan")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your PersonelLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 11
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            t = input("So you have paid all amount.Yes or No:")
            if t == "Yes":
                print("Thank you for paying.Hope that we will meet you again")
                cursor.execute("""DELETE
                      FROM PERSONELLOAN
                      WHERE personelLoanId like {}""".format(c))
                Mycon.commit()
                print("===============================================================")
                continue
            else:
                print("Hope that you will pay soon.Thank You")
                print("==============================================================")
                continue
        else:
            print("So you have taken gold loan")
            u = int(input("Enter your LoanId:"))
            c = int(input("Enter your GoldLoanId:"))
            months = int(input("Enter number of months from when you had taken loan or repayed some amount:"))
            r = remainingamount(u)
            n = 1
            b = balance(r, months, n)

            print("The remaing amount that you have to pay is:", b)
            t = input("So you have paid all amount.Yes or No:")
            if t == "Yes":
                print("Thank you for paying.Hope that we will meet you again")
                cursor.execute("""DELETE
                      FROM GOLDLOAN
                      WHERE goldLoanId like {}""".format(c))
                Mycon.commit()
                print("================================================================")
                continue
            else:
                print("Hope that you will pay soon.Thank You")
                print("==================================================================")
                continue

    elif n == 5:
        print("So you want to check  details of customers")
        password = int(input("Enter password to see details:"))
        if password == 1234:
            result = cursor.execute("select* from loan")
            info = cursor.fetchall()
            for i in info:
                print(i)
            ids = int(input("Enter Loan id of the person that you want to  see"))
            idetails(ids)
            print("===================================================================")
            continue

        else:
            print("You entered a wrong password")
            print("====================================================================")
            continue
    elif n == 6:
        print("Thank you for using CSSSP's Loan Management System")
        print("================================================================")
        break
    else:
        print("You Entered a wrong choice!!!,Please re-enter your choice.")
        print("========================================================================")
        continue
