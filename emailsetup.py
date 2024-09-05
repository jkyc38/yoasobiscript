import smtplib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email content
subject = "Test Email from Python"
body = "This is a test email sent from Python using smtplib."



def send_email(from_email, to_email, body, subject):
    app_password = 'PASSWORD'
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(from_email, app_password)  # Log in to the server
            server.sendmail(from_email, to_email, message.as_string())  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")