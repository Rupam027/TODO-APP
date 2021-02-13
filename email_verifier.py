from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
import smtplib 






def send_confirmation_mail(user_email , otp , link):
    sender_id = 'dopplerlife945@gmail.com' 
    password = 'Rupam2000' 
    receiver_id = user_email

    

    email = MIMEMultipart()
    email['From']= sender_id
    email['To'] =  receiver_id 
    email['Subject'] = 'EMAIL VERICATION' 

    body = 'OTP to reset your password is : {} . Click on this {} to reset your password . This is a system generated mail. Please do not reply.'.format(otp , link)

    email.attach(MIMEText(body , 'plain'))
    


    txt = email.as_string() 

            
    server = smtplib.SMTP_SSL('smtp.gmail.com') 
    
    try:
        server.login(sender_id , password) 
        

        server.sendmail(sender_id , receiver_id , txt)
        server.quit()
    except Exception as e:
        print(e)
        
        
        

    
