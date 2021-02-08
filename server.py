from flask import Flask , render_template , request , redirect , url_for , session
import json
from dbcheck import *

app =   Flask(__name__) 
app.secret_key = 'az75z8962df1235s'

message = ''
exist = ''

@app.route('/')
def home():
    global message
    global exist
    message = ''
    exist = ''
    return render_template('index.htm') 



@app.route('/register')
def register(): 
    
    return render_template('reg.htm' ,error=exist) 


@app.route('/login')    
def login():
    
    global message
    if "user" in session:
        username = session['user'] 
        user = check(username)
        activity = user["activity"]
        return render_template('profile.htm' ,user=username,data=activity)
     
    return render_template('login.htm' ,error=message) 



@app.route('/create-account' , methods=['POST'])
def create():
    global exist
    data = request.form 
    name = data['full']
    user = data['user']
    
    password = data['pass'] 
    c = check(user)
    if c == -1: 
        exist = ''
        d = {} 
        d["name"] = name 
        d["user"] = user 
        d["password"] = password 
        d["activity"] = []
        
        insert(d) ; 
        session["user"] = user ; 
        
        return redirect(url_for('profile'))
    else: 
        exist = 'Username already exist' 
        return redirect(url_for('register'))



@app.route('/profile')
def profile():
    if "user" in session:
        username = session['user'] 
        user = check(username)
        activity = user["activity"]
        
        return render_template('profile.htm' ,user=username,data=activity) 
    else:
        return redirect(url_for('register'))


@app.route('/check' ,methods = ['POST'])    
def check_cred(): 
    global message
    data = request.form
    usr = data['user']
    pas = data['pass']
    user = check(usr) 
    if user != -1:
        username = user['user']
        password = user['password']
        
    
        if pas == password: 
            message = ''
            session['user'] = username  
            return redirect(url_for('profile'))
        else: 
            message = 'Invalid Username and password' 
            return redirect(url_for('login'))
            
    else : 
        message = 'Invalid Username and password'
        return redirect(url_for('login'))
    
@app.route('/create' , methods=['POST']) 
def createtask():
    task_info = request.form 
    taskname = task_info["task"]
    deadline = task_info["deadline"] 
    urgency  = task_info["urgent"]
    username = session["user"] 
    activity = {} 
    
    activity["task"] = taskname  
    activity["urgency"] = urgency
    activity["deadline"] = deadline 
    
    update_activity(username , activity) 
    return redirect(url_for('profile'))
    
@app.route('/delete' , methods=['POST'])
def deletetask():
    username = session["user"]
    form = request.form
    activity_index = int(form["delete"])
    delete_activity(username , activity_index)
    return redirect(url_for('profile')) 
    
    
    
    

    

    
if __name__ == '__main__' : 
    
    app.run(debug = True)