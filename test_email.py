# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:51:57 2021

@author: garvi
"""

from email.message import EmailMessage
import smtplib
import os
import random
from dotenv import load_dotenv
from quote import quote

load_dotenv(".env")

SENDER = "garvitjairath@gmail.com"
PASSWORD = "30july99J"

def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = recipient
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER, PASSWORD)
    server.send_message(msg)
    server.quit()

body = "U is gay"

send_email("garvitjairath@gmail.com", subject="Quote of the Day", body=body)
