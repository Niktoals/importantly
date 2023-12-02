from Data import DataBase
from fuzzywuzzy import fuzz
import os
import smtplib
import os
import time
import mimetypes
from tqdm import tqdm
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase





def creating_ban_list(file, db):
    
    ban_message_list = ["сука", "украина"]
    file = open(file, 'w', encoding='utf-8')
    list_of_messages = [x for x in db.search_message()]
    for checker in ban_message_list:
        for message in list_of_messages:
            if fuzz.partial_ratio(message[0], checker)>=80:
                file.write(f"Человек с ID = {message[1]} отправил такое сообщение '{message[0]}'\n")
    file.close()

def send_email(file=None):
    
    sender = "to.artik.mp@gmail.com"
    password = "qrfz fach hhrn bzgc"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        with open(file, 'r', encoding='utf-8') as f:
            template = MIMEText(f.read())
    except IOError:
        template = None

    try:
        server.login(sender, password)
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = sender
        msg["Subject"] = f"Ban_list по боту за {time.strftime('%c')}"

        if template:
            template.add_header('content-disposition', 'attachment', filename=file)
            msg.attach(template)

        print("Sending...")
        server.sendmail(sender, sender, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"










