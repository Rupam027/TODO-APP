from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
import smtplib 
import random





def send_confirmation_mail(user_email):
    sender_id = 'dopplerlife945@gmail.com' 
    password = 'Rupam2000' 
    receiver_id = user_email

    otp = random.randint(1000 , 9999) 

    email = MIMEMultipart()
    email['From']= sender_id
    email['To'] =  receiver_id 
    email['Subject'] = 'EMAIL VERICATION' 

    body = 'Your 4 digit otp : {} . This is a system generated mail. Please do not reply.'.format(otp)

    email.attach(MIMEText(body , 'plain'))
    


    txt = email.as_string() 

            
    server = smtplib.SMTP_SSL('smtp.gmail.com') 
    
    try:
        server.login(sender_id , password) 
        

        server.sendmail(sender_id , receiver_id , txt)
        server.quit()
    except Exception as e:
        print(e)
        
        
        
import datetime    
if __name__ == '__main__':
    print(datetime.datetime.now())
    send_confirmation_mail('sadhu2gourish@gmail.com')
    print(datetime.datetime.now())
    
