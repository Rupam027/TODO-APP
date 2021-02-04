from flask import Flask , render_template , request , redirect , url_for
import json

app =   Flask(__name__) 


message = ''


@app.route('/')
def home():
    return render_template('index.htm') 


@app.route('/register')
def register(): 
    return render_template('reg.htm') 

@app.route('/login')    
def login():
    global message
    return render_template('login.htm' ,error=message) 


    
@app.route('/profile' ,methods = ['POST'])
def profile():
    
    global message 
    data = request.form
    usr = data['user']
    pas = data['pass']
    
    f = open('data.json') 
    db = json.load(f) 
    user1 = db[0]
    activity = user1["activity"]
    
    if (usr == user1['user']) and (pas == user1['password']) : 
        message = ''
        return render_template('profile.htm' ,user=usr,data=activity)
    else : 
        message = 'Invalid Username and password'
        return redirect(url_for('login'))
     
        
    

if __name__ == '__main__' : 
    
    app.run(debug = True)