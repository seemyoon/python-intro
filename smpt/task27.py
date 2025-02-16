import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html_template = Template(Path("templates/template.html").read_text())

html_content = html_template.substitute({"name": "Oleksandr", "date": "tomorrow"})

my_email = EmailMessage()

my_email["from"] = "Oleksandr"
my_email["to"] = "test@test.com"
my_email["subject"] = "hello from python"
my_email.set_content(html_content, "html")

with smtplib.SMTP(host="127.0.0.1", port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("email was sent")
