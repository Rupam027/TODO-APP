from flask import Flask , render_template , request , redirect , url_for , session
import json
from dbcheck import *
from passlib.hash import pbkdf2_sha256
import datetime
from email_verifier import *
import random

app =   Flask(__name__) 
app.secret_key = 'az75z8962df1235s'

message = ''
exist = ''
email_error = ''
otp_error = ''
otp = None

@app.route('/')
def home():
    global email_error
    global message
    global exist
    global invalid 
    global otp_error 
    
    otp_error = ''
    email_error = ''
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
   
        return redirect(url_for('profile'))
    
    else:
        return render_template('login.htm' ,error=message) 
    
        



@app.route('/create-account' , methods=['POST'])
def create():
    global exist
    
    
    data = request.form 
    name = data["full"]
    user = data["user"]
    email = data["email"]
    
    
    password = data['pass']
     
    c1 = check(user)
    c2 = check(email)
    if (c1 == -1) and (c2 == -1): 
        
        exist = ''
        d = {} 
        d["name"] = name 
        d["user"] = user 
        d["password"] = password
        d["email"] = email 
        d["activity"] = []
        
        insert(d)  
        session["user"] = user
        
        
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
        date = str(datetime.datetime.now())
        date = date.split(' ')[0]
        print(date)
        return render_template('profile.htm' ,user=username,data=activity,date=date) 
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
        
        
        if pbkdf2_sha256.verify(pas , password): 
            message = ''
            session['user'] = username  
            return redirect(url_for('profile'))
        else: 
            message = 'Invalid credentials' 
            return redirect(url_for('login'))
            
    else : 
        message = 'Invalid credentials'
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

@app.route('/logout')   
def logout():
    session.pop("user")
    return redirect(url_for('home'))
    
@app.route('/forgotpassword') 
def forgotpassword():
    global message 
    message = ''
    global email_error
    return render_template('reset.htm' ,emailerror=email_error)
 
    
@app.route('/email' , methods = ['POST']) 
def send_mail(): 
    global email_error
    global otp
    email = request.form["email"] 
    c = check(email) 
    if(c != -1):
        user = c["user"]
        email_error = '' 
        link = "http://127.0.0.1:5000/reset/"+user
        otp = random.randint(1000 , 9999)
        send_confirmation_mail(email , otp , link)
        return redirect(url_for('forgotpassword'))
    else:
        email_error = 'EMAIL NOT REGISTERED' 
        return redirect(url_for('forgotpassword'))

@app.route('/reset/<username>') 
def reset_password(username):
    global otp_error
    return render_template('change.htm' ,user=username,otperror=otp_error)
    
@app.route('/changepassword' , methods = ['POST']) 
def reset():
    global otp 
    global otp_error
    data = request.form
    if int(data["otp"]) == otp: 
        otp = None
        otp_error = ''
        update_password(data["user"] , data["new"])
        return redirect(url_for('login'))
    else: 
        otp_error = "INVALID OTP"
        user = data["user"]
        rd = '/reset/'+user 
        return redirect(rd)
        
    
    
    

    
if __name__ == '__main__' : 
    
    app.run(debug = True)