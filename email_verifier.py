from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
import smtplib 






def send_confirmation_mail(user_email , otp , choice):
    sender_id = 'dopplerlife945@gmail.com' 
    password = 'Rupam2000' 
    receiver_id = user_email
    strotp = str(otp)
    ls = list(strotp)
    print(ls)
    subject = ''
    if choice == 1:
        subject = 'RESET PASSWORD'
        html = '''<html>
                <head></head>
                <body style="background-color:#2EFEF7;">
                <h2 style="background-color:#0101DF;" > <center> <em> Your 4 digit code to reset your password </em> </center>  </h2>
                <br/> 

                <center> <label style="font-size:50px;" > <u> {} </u> &nbsp; <u> {} </u> &nbsp; <u> {} </u> &nbsp; <u> {} </u> </label> </center>
                <br/>
                <center> <small> <em> This code is valid only for once . Incorrect Tries not allowed. </em> </small> </center>
                <br/>
                <center> <img src="https://media.giphy.com/media/jwXoaQKjk9L1i8btPi/giphy.gif" width=50% height=50% alt="gif" /> </center>
                </body>
                </html> ''' 
    else:
        subject = 'EMAIL VERIFICATION'
        html = '''<html>
                <head></head>
                <body style="background-color:#2EFEF7;">
                <h2 style="background-color:#0101DF;" > <center> <em> Verify your email </em> </center>  </h2>
                <br/> 

                <center> <label style="font-size:50px;" > <u> {} </u> &nbsp; <u> {} </u> &nbsp; <u> {} </u> &nbsp; <u> {} </u> </label> </center>
                <br/>
                <center> <small> <em> This code is valid only for once . Incorrect Tries not allowed. </em> </small> </center>
                <br/>
                <center> <img src="https://media.giphy.com/media/jwXoaQKjk9L1i8btPi/giphy.gif" width=50% height=50% alt="gif" /> </center>
                </body>
                </html> '''
        
    

    email = MIMEMultipart()
    email['From']= sender_id
    email['To'] =  receiver_id 
    email['Subject'] = subject

    body = html.format(ls[0] ,ls[1] ,ls[2] ,ls[3])

    email.attach(MIMEText(body , 'html'))
    


    txt = email.as_string() 

            
    server = smtplib.SMTP_SSL('smtp.gmail.com') 
    
    try:
        server.login(sender_id , password) 
        

        server.sendmail(sender_id , receiver_id , txt)
        server.quit()
    except Exception as e:
        print(e)
        
