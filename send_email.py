import smtplib

sender_email = ""
sender_password = ""  
recipient_email = ""

subject = "Test"
body = "This is a test email."

email_content = f"Subject: {subject}\n\n{body}"

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  
        server.login(sender_email, sender_password)  
        server.sendmail(sender_email, recipient_email, email_content)  
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")