from flask import Flask , render_template , request , redirect , url_for , session , flash
from dbcheck import *
from passlib.hash import pbkdf2_sha256
import datetime
from email_verifier import *
import random

app =   Flask(__name__) 
app.secret_key = 'az75z8962df1235s'

@app.route('/')
def home():
    return render_template('index.htm') 



@app.route('/register')
def register(): 
    
    return render_template('reg.htm') 


@app.route('/login')    
def login():
    
    global message
    if "user" in session:
   
        return redirect(url_for('profile'))
    
    else:
        return render_template('login.htm' , disp1="None" , disp2="block" ) 
    
        



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
        flash('Username already exist') 
        return redirect(url_for('register'))
    


    
    
@app.route('/profile')
def profile():
    if "user" in session:
        username = session['user'] 
        user = check(username)
        activity = user["activity"]
        date = str(datetime.datetime.now())
        date = date.split(' ')[0]
        email = user["email"]
        
        return render_template('profile.htm' ,user=username,data=activity,date=date) 
    else:
        return redirect(url_for('login'))


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
            
            session['user'] = username  
            return redirect(url_for('profile'))
        else: 
            flash('Invalid credentials') 
            return redirect(url_for('login'))
            
    else : 
        flash('Invalid credentials')
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
    
    return render_template('reset.htm')
 
    
@app.route('/email' , methods = ['POST']) 
def send_mail(): 
    
    email = request.form["email"] 
    c = check(email) 
    if(c != -1):
        
        user = c["user"]
        popotp(user)
        link = "/reset/"+user
        otp = random.randint(1000 , 9999)
        send_confirmation_mail(email , otp , 1)
        pushotp(user,otp)
        return redirect(link)
    else:
        flash('EMAIL NOT REGISTERED')
        return redirect(url_for('forgotpassword'))

@app.route('/reset/<username>') 
def reset_password(username):
    
    return render_template('change.htm' ,user=username)
    
@app.route('/changepassword' , methods = ['POST']) 
def reset():
     
    
    data = request.form
    user = data['user']
    entered = int(data['otp'])
    otp = getotp(user)
    
    if entered == otp: 
        popotp(user)
        update_password(data["user"] , data["new"])
        return redirect(url_for('login'))
    else:
        popotp(user)
        flash('INVALID OTP')
        user = data["user"]
        rd = '/reset/'+user 
        return redirect(rd)

@app.route('/send-otp/<req>')
def get_otp(req):
    print("I am otp" , req)
    email , otp = req.split('&')
    send_confirmation_mail(email , otp , 2)
    return '' , 204 
    

import os
if __name__ == '__main__' :
    
    os.environ["HOST"] = "sql12.freesqldatabase.com"
    os.environ["DATABASE_USER"] = "sql12393651"
    os.environ["DATABASE_NAME"] = "sql12393651"
    os.environ["DATABASE_PASSWORD"] = "YFCJsfc9eJ"
    app.run(debug=True)

    
    
    