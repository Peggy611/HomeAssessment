#! /usr/bin/python

import mysql.connector
import datetime

def Fetch_TaxRelief():
#connect to database
    mydb = mysql.connector.connect(
        host="hostname",
        user="username",
        password="password",
        database="databasename"
    )

    mycursor = mydb.cursor()
#fetch necessary value from database by name(my name as example)
    sql = "SELECT Gender,Birthday,Salary,TaxPaid FROM WorkingClassHero WHERE Name ='Peggy Zhu'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        hgender = x[0]
        hbirthday = x[1]
        hsalary = x[2]
        htaxpaid = x[3]

    #if gender is female, genderbonus is 500, else it's 0
    Genderbonus=0
    if hgender == "Female":
        Genderbonus=500


    #calculate the age from birthday year to 1969, strptime to convert string to datetime
    datem = datetime.datetime.strptime(hbirthday, "%Y-%m-%d %H:%M:%S")
    age = 1969-datem.year

    # decide variable based on age
    if age <= 18:
        hvariable = 1
    elif age <= 35:
        hvariable = 0.8
    elif age <=50:
        hvariable = 0.5
    elif age <= 75:
        hvariable = 0.367
    else:
        hvariable = 0.05

    #calculate raw taxrelief
    taxrelief = (hsalary-htaxpaid) * hvariable + Genderbonus

    #do normal rounding rule for 2 decimal points
    for i in [2,1,0]:
        taxrelief=round(taxrelief,i)

    #if taxrelief is less than 50, it will be given to 50
    if taxrelief<50:
        taxrelief=50

    print(taxrelief)
    return taxrelief
