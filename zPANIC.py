import smtplib
from email.message import EmailMessage
import sys

try:
    import zpass
except:
    print("ERROR: credentials file missing.")
    print("Create a 'zpass.py' file with the following content:\n")
    print("FROM = your@email.com'        # custom sender email")
    print("PASS = 'xxxx xxxx xxxx xxxx'  # custom app password")
    print("TO = 'receiver@email'         # custom default receiver email\n")
    print("Use example:")
    print("python3 ~/zPANIC/zPANIC.py 'another@email.com' && exit\n")
    

def alert(to, subject='ALERT', content=None, attachment=None):
    msg = EmailMessage()
    msg['From'] = zpass.FROM
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(content)

    if attachment:
        with open(attachment, 'rb') as pdf:
            msg.add_attachment(pdf.read(), maintype='application', subtype='octet-stream', filename=pdf.name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(zpass.FROM, zpass.PASS) 
        smtp.send_message(msg)
    
    print(f"Alert sent to {to}")

if __name__ == "__main__":

    to = zpass.TO
    subject = 'PANIC ALERT'
    content = 'PANIC BUTTON ACTIVATED'
    attachment = None

    if len(sys.argv) > 1:
        to = sys.argv[1]
    if len(sys.argv) > 2:
        subject = sys.argv[2]
    if len(sys.argv) > 3:
        content = sys.argv[3]
    if len(sys.argv) > 4:
        attachment = sys.argv[4]

    alert(to, subject, content, attachment)

