# Automated Email Sender Script

This project is a Python-based script to send automated emails with custom messages and optional attachments. It leverages the `smtplib` library for SMTP communication and ensures email security by using environment variables to manage sensitive credentials.

## Features
- Send emails to any recipient.
- Include custom subject lines and message bodies.
- Attach files to your emails (optional).
- Securely store and access credentials using `.env` files.

## Prerequisites
1. **Python**: Ensure Python 3.7+ is installed on your system.
2. **Required Libraries**: Install the dependencies using:
   ```bash
   pip install python-dotenv
   ```
3. **Gmail App Password**: If using Gmail, enable 2-Step Verification and generate an [App Password].

## Getting Started
### 1. Clone the Repository

### 2. Set Up the Environment
Create a `.env` file in the project directory and add your email credentials:
```env
EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=your-app-password
```

### 3. Usage
Customise and run the script:
```bash
python send_email.py
```

### Example Code
```python
# Sending a basic email
receiver = "receiver@example.com"
subject = "Hello, Peter"
body = "Dear Peter,\nThis is an automated email sent from Python!\n\nBest regards,\nYour Name"
attachment = None  # Optional, specify a file path for attachments
send_email(receiver, subject, body, attachment)
```

## File Structure
```
.
├── send_email.py         # Main Python script
├── .env                  # Environment file for storing credentials (not shared)
├── README.md             # Project documentation
```

## How It Works
1. **SMTP Server**: Connects to Gmail's SMTP server (`smtp.gmail.com`) to send emails.
2. **Email Composition**: Uses `email.mime` to create well-formatted emails.
3. **Security**: Credentials are securely accessed using `dotenv` to avoid hardcoding.

## Troubleshooting
### Common Errors
1. **Authentication Error (534)**: Ensure you use a valid App Password for Gmail.

### Debugging Tips
- Check your `.env` file for typos or incorrect credentials.
- Review Gmail security settings and enable access for less secure apps (if not using 2FA).
