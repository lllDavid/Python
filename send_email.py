import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = ""
sender_password = ""  
recipient_email = ""

subject = "Test"
body = "This is a test email."

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  
        server.login(sender_email, sender_password)  
        server.send_message(msg) 
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")
