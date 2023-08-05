###importing mysql.connector to connect python with mysql database###
 
import mysql.connector as sqltor

###importing tabulate for showing output data in the form of tables###

from tabulate import tabulate

###importing sys and os to ineract with th operating system

import sys
import os

##establishing connection of python with database

connection=sqltor.connect(host="localhost",user="root",password="******",database="software") 
cursor=connection.cursor()

# BLOCK FOR INSERTING THE DATA

def Add_Record(): 
    p_id=(input("Enter the parking number :  ")) 
    
    p_name=input("Enter the  Parking Name: ") 
    
    level=input("Enter level of parking : ") 
    
    vehicle_no=input("Enter the Vehicle Number : ") 
    
    checkin=input('Enter the date and time of checkin as (yyyy-mm-ddhh:mm:ss):')

    checkout=input('Enter the date and time of checkout as (yyyy-mm-ddhh:mm:ss):')

    ## SQL Query

    sql="insert into parking_det (p_id,p_name,level,veh_no,checkin,checkout)values('{}','{}','{}','{}','{}','{}')".format(p_id,p_name,level,vehicle_no,checkin,checkout) 
    
    cursor.execute(sql) 
    
    connection.commit()
    
    connection.close()
    
    
# BLOCK FOR VIEWING THE DATA
    
def RecView(): 
    print("\nSelect the search criteria : ") 
    print("\n1. Parking  Number") 
    print("2. Parking Name") 
    print("3. Level No") 
    print("4. All") 
    
    ch=(input("Enter the choice : ")) 
    
  #FOR VIEWING DATA USING PARKING NUMBER  
  
    if ch=='1': 
        s=(input("\nEnter Parking no : ")) 
        
        #SQL Query
        sql="select * from parking_det where p_id='{}';".format(s)
        
        print("\nDetails  about Parking are as follows : ")
        cursor.execute(sql)
        data=cursor.fetchall()
        print(tabulate(data,headers=['p_id','p_name','level','veh_no','checkin','checkout'],tablefmt='orgtbl',colalign='right'))
    
    
   #FOR VIEWING DATA USING PARKING NAME
   
    elif ch=='2':  
        s=input("\nEnter Parking Name : ")  
        
        #SQL Query
        sql="select * from parking_det where p_name='{}';".format(s) 
       
        print("\nDetails  about Parking are as follows : ")
        cursor.execute(sql)
        data=cursor.fetchall()
        print(tabulate(data,headers=['p_id','p_name','level','veh_no','checkin','checkout'],tablefmt='orgtbl',colalign='right'))
    
            
   #FOR VIEWING DATA USING LEVEL OF PARKING   
      
    elif ch=='3': 
        s=int(input("\nEnter Level  of Parking : "))
        
        #SQL Query
        sql="select * from parking_det where level='{}'".format(s)
        
        print("\nDetails  about Parking are as follows : ") 
        cursor.execute(sql)
        data=cursor.fetchall()
        print(tabulate(data,headers=['p_id','p_name','level','veh_no','checkin','checkout'],tablefmt='orgtbl',colalign='centre'))
    
            
    #FOR VIEWING  THE DATA OF ALL VEHICLES    
    
    elif ch=='4': 
        
        #SQL Query
        sql="select * from parking_det;"
        
        print("\nDetails  about Parking are as follows : ") 
        cursor.execute(sql)
        data=cursor.fetchall()
        print(tabulate(data,headers=['p_id','p_name','level','veh_no','checkin','checkout'],tablefmt='orgtbl',colalign='centre'))
        
    #IF CHOICE IS NOT THERE
    
    else:
        print('INVALID CHOICE!!!!!!!!!!!!!!')
#   runAgain()

    
        
# BLOCK FOR ADDING VEHICLE DETAIL
        
def Vehicle_Detail(): 

    v_id=(input("Enter Vehicle No : ")) 
  
    v_name=input("Enter Vehicle Name/Model Name : ") 
  
    date_of_purchase=input("Enter  Date of purchase(yyyy-mm-dd) : ") 
    
    #SQL Query
    sql="insert into vehicle (veh_no,v_name,date_of_purchase) values ('{}','{}','{}')".format(v_id,v_name,date_of_purchase)
    cursor.execute(sql) 
    connection.commit() 
    connection.close()

      
# BLOCK FOR VIEWING VEHICLE DETAILS
    
def Vehicle_View(): 
    v_id=(input("Enter the vehicle number of the vehicle whose details is to be viewed : ")) 
    
    #SQL Query
    sql=("Select p_id,p_name,level,v_no,v_name,date_of_purchase from parking_det ,vehicle_det where v_no='{}' and veh_no='{}'".format(v_id,v_id))
   
    cursor.execute(sql) 
    data=cursor.fetchall()
    print(tabulate(data,headers=['p_id','p_name','level','v_no','v_name','date_of_purchase'],tablefmt='orgtbl',colalign='centre'))
    connection.close()    


# BLOCK FOR DELETING A VEHICLE DETAIL
    
def remove(): 
    v_id=(input("\nEnter the vehicle number of the vehicle  to be deleted : ")) 
    sql="Delete from vehicle_det where v_no='{}'".format(v_id) 
    cursor.execute(sql) 
    connection.commit()
    connection.close()

##BLOCK FOR CHOICES

def Menu(): 
    print("Enter 1 : To Add Parking Detail") 
    print("Enter 2 : To View Parking Detail ") 
    print("Enter 3 : To Add Vehicle Detail ") 
    print("Enter 4 : To Remove  Vehicle Record") 
    print("Enter 5 : To see the details of Vehicle") 
    
    input_dt = int(input("\nPlease Select An Above Option: "))
                                   
    if(input_dt== 1):                        ##IF CHOICE IS 1
        Add_Record() 
        
    elif (input_dt==2):                      ##IF CHOICE IS 2
        RecView() 
        
    elif (input_dt==3):                      ##IF CHOICE IS 3
        Vehicle_Detail() 
        
    elif (input_dt==4):                      ##IF CHOICE IS 4 
        remove() 
        
    elif (input_dt==5):                       ##IF CHOICE IS 5 
        Vehicle_View() 
        
    else:                                     ##IF THE CHOICE IS NOT GIVEN IN THE OPTION
        print("\nEnter correct choice. . . ") 
       
Menu() 

##BLOCK TO RUN AGAIN THE PROGRAM
def restart_program():
   
    """Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
   
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
if __name__ == "__main__":
    answer = input("\n Do you want to restart this program ? ")
    
    if answer.lower().strip() in "y yes".split():                 ##IF WANT TO RESTART
        restart_program()

