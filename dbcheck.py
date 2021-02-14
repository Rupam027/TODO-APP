import json
import sqlite3
from passlib.hash import pbkdf2_sha256


    
    

def insert(d): 
    
    conn = sqlite3.connect('todo.db')
    insert_query = "INSERT INTO User(username,Name,password ,email) VALUES('{}' , '{}' , '{}' , '{}');"
    d["password"] = pbkdf2_sha256.hash(d["password"])
    
    formatted = insert_query.format(d["user"] , d["name"] ,d["password"] , d["email"])
    conn.execute(formatted) 
    conn.commit()
    conn.close()
    
    
    
    
def check(user):
    
    d = {}
    conn = sqlite3.connect('todo.db')
    select_userquery = "SELECT * FROM User WHERE username = '{}' OR email = '{}' ;"
    select_activity  = "SELECT * FROM Activity WHERE user = '{}' ;"
    formatted = select_userquery.format(user , user , 1) 
    formatted1 = select_activity.format(user)
    
    
    ls = list(conn.execute(formatted))
    ls1 = list(conn.execute(formatted1))
    if len(ls) > 0:
        d["name"] =  ls[0][1]
         
        d["user"] = ls[0][0]
        d["password"] = ls[0][2]
        d["activity"]= ls1
        return d
        
    else:
        return -1
    conn.close()
        
        
def update_activity(username , activity):
    
    conn = sqlite3.connect('todo.db')
    insert_query = "INSERT INTO Activity(Taskname , Urgency ,Deadline ,user) VALUES('{}' , '{}' , '{}' , '{}');"
    
    formatted = insert_query.format(activity["task"] , activity["urgency"] ,activity["deadline"] ,username)
    conn.execute(formatted) 
    conn.commit()
    conn.close()
    
    
def delete_activity(username , index):
    conn = sqlite3.connect('todo.db')
    delete_query = "DELETE FROM Activity WHERE user='{}' AND id = '{}';"
    
    
    formatted = delete_query.format(username , index)
    conn.execute(formatted) 
    conn.commit()
    conn.close()
    
def update_password(user , password):
    conn = sqlite3.connect('todo.db')
    password = pbkdf2_sha256.hash(password)
    update_query = "UPDATE User SET password = '{}' WHERE  username = '{}';"
    
    formatted = update_query.format(password , user)
    conn.execute(formatted) 
    conn.commit()
    conn.close()
    
def pushotp(user , otp):
    conn = sqlite3.connect('todo.db')
    push = "INSERT INTO UserOTP(user , otp) VALUES('{}' , '{}');" 
    formatted = push.format(user , otp)
    conn.execute(formatted) 
    conn.commit()
    conn.close()
    
def getotp(user):
    conn = sqlite3.connect('todo.db')
    select = "SELECT otp FROM UserOTP WHERE user = '{}' ;" 
    formatted = select.format(user)
    otp = list(conn.execute(formatted))
    if(len(otp) == 0):
        conn.close()
        return None
    else:
        otp = otp[0][0]
        conn.close()
        return otp  
    
def popotp(user):
    conn = sqlite3.connect('todo.db')
    delete = "DELETE FROM UserOTP WHERE user = '{}' ;" 
    formatted = delete.format(user)
    conn.execute(formatted) 
    conn.commit()
    conn.close()
    
    
    
    

    
    
    
    
    
if __name__ == '__main__': 
    print(check('prasad'))