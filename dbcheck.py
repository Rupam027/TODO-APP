import json
import sqlite3
from passlib.hash import pbkdf2_sha256


    
    

def insert(d): 
    
    conn = sqlite3.connect('todo.db')
    insert_query = "INSERT INTO User(username,Name,password) VALUES('{}' , '{}' , '{}');"
    d["password"] = pbkdf2_sha256.hash(d["password"])
    
    formatted = insert_query.format(d["user"] , d["name"] ,d["password"])
    conn.execute(formatted) 
    conn.commit()
    
    
    
    
def check(user):
    
    d = {}
    conn = sqlite3.connect('todo.db')
    select_userquery = "SELECT * FROM User WHERE username = '{}' ;"
    select_activity  = "SELECT * FROM Activity WHERE user = '{}' ;"
    formatted = select_userquery.format(user) 
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
    
        
        
def update_activity(username , activity):
    
    conn = sqlite3.connect('todo.db')
    insert_query = "INSERT INTO Activity(Taskname , Urgency ,Deadline ,user) VALUES('{}' , '{}' , '{}' , '{}');"
    
    formatted = insert_query.format(activity["task"] , activity["urgency"] ,activity["deadline"] ,username)
    conn.execute(formatted) 
    conn.commit()
    
    
def delete_activity(username , index):
    conn = sqlite3.connect('todo.db')
    delete_query = "DELETE FROM Activity WHERE user='{}' AND id = '{}';"
    
    
    formatted = delete_query.format(username , index)
    conn.execute(formatted) 
    conn.commit()
    
    
    
    
    
if __name__ == '__main__': 
    print(check('prasad'))