import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

# Load email credentials from .env file (optional)
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  # Sender's email address
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Sender's email password

def send_email(receiver_email, subject, body, attachment_path=None):
    try:
        # 1. Set up email headers
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # 2. Add the email body
        msg.attach(MIMEText(body, 'plain'))

        # 3. Attach a file (optional)
        if attachment_path:
            with open(attachment_path, 'rb') as file:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(file.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
                msg.attach(attachment)

        # 4. Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())
            print(f"Email sent successfully to {receiver_email}!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage example
if __name__ == "__main__":
    receiver = "receiver@example.com"
    subject = "Test Email"
    body = "Hi, this is an automated email sent from Python."
    attachment = "example.pdf"  # Optional, path to a file

    send_email(receiver, subject, body, attachment)
