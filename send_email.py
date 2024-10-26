import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "your_email@gmail.com"
sender_password = "your_password"  # Use app password for Gmail
recipient_email = "recipient@example.com"

# Create the email
subject = "Test Email"
body = "This is a test email sent from a Python script."

# Setup the MIME
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Enable security
        server.login(sender_email, sender_password)  # Login
        server.send_message(msg)  # Send email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
