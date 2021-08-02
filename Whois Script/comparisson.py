import json
import os
import pathlib
import filecmp
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

path = pathlib.Path(__file__).parent.absolute()
current_path = str(path)

#domains to be compared. There are 2 files per domain, that will be compared each 24 hrs
builradat_domain = "{}/data_domain_www.buildarat.com_0.json".format(current_path)
builradat_domain_2 = "{}/data_domain_www.buildarat.com_1.json".format(current_path)

disorderstatus_domain = "{}/data_domain_www.disorderstatus.ru_0.json".format(current_path)
disorderstatus_domain_2 = "{}/data_domain_www.disorderstatus.ru_1.json".format(current_path)

garatinterbk_domain = "{}/data_domain_www.garatinterbk.online_0.json".format(current_path)
garatinterbk_domain_2 = "{}/data_domain_www.garatinterbk.online_1.json".format(current_path)

hngleg_domain = "{}/data_domain_www.hngleg.online_0.json".format(current_path)
hngleg_domain_2 = "{}/data_domain_www.hngleg.online_1.json".format(current_path)

pionsecar_domain = "{}/data_domain_www.pionsecar.com_0.json".format(current_path)
pionsecar_domain_2 = "{}/data_domain_www.pionsecar.com_1.json".format(current_path)




#--------------------------------------------------------------#


def read_domain_1():
    flag = False
    # Opening JSON file for domain #1
    f = open(builradat_domain,)
    # returns JSON object as dict
    data = json.load(f)
    createdDate = data['WhoisRecord']['createdDate']
    updatedDate = data['WhoisRecord']['updatedDate']
    expiresDate = data['WhoisRecord']['expiresDate']
    email = data['WhoisRecord']['contactEmail']
    if(not email):
        email = "no emails registered"
    f.close()

    f2 = open(builradat_domain_2,)
    data1 = json.load(f2)
    createdDate_1 = data1['WhoisRecord']['createdDate']
    updatedDate_1 = data1['WhoisRecord']['updatedDate']
    expiresDate_1 = data1['WhoisRecord']['expiresDate']
    email_1 = data1['WhoisRecord']['contactEmail']
    if(not email_1):
        email_1 = "no emails registered"
    f2.close()

    if(createdDate != createdDate_1 or updatedDate != updatedDate_1 or expiresDate != expiresDate_1 ):
        flag = True

    return flag


#--------------------------------------------------------------#

def read_domain_2():
    flag = False
    # Opening JSON file for domain #2
    f3 = open(disorderstatus_domain,)
    # returns JSON object as dict
    data = json.load(f3)
    createdDate_2 = data['WhoisRecord']['audit']['createdDate']
    updatedDate_2 = data['WhoisRecord']['audit']['updatedDate']
    expiresDate_2 = data['WhoisRecord']['registryData']['expiresDate']

    f3.close()

    f4 = open(disorderstatus_domain_2,)
    data1 = json.load(f4)
    createdDate_3 = data1['WhoisRecord']['audit']['createdDate']
    updatedDate_3 = data1['WhoisRecord']['audit']['updatedDate']
    expiresDate_3 = data1['WhoisRecord']['registryData']['expiresDate']

    f4.close()

    if(createdDate_2 != createdDate_3 or updatedDate_2 != updatedDate_3 or expiresDate_2 != expiresDate_3):
        flag = True

    return flag

#--------------------------------------------------------------#

def read_domain_3():
    flag = False
    # Opening JSON file for domain #3
    f5 = open(garatinterbk_domain,)
    # returns JSON object as dict
    data = json.load(f5)
    createdDate_4 = data['WhoisRecord']['audit']['createdDate']
    updatedDate_4 = data['WhoisRecord']['audit']['updatedDate']
    expiresDate_4 = data['WhoisRecord']['registryData']['expiresDate']
    email_4 = data['WhoisRecord']['contactEmail']
    if(not email_4):
        email_4 = "no emails registered"
    f5.close()

    f6 = open(garatinterbk_domain_2,)
    data1 = json.load(f6)
    createdDate_5 = data1['WhoisRecord']['audit']['createdDate']
    updatedDate_5 = data1['WhoisRecord']['audit']['updatedDate']
    expiresDate_5 = data1['WhoisRecord']['registryData']['expiresDate']
    email_5 = data1['WhoisRecord']['contactEmail']
    if(not email_5):
        email_5 = "no emails registered"
    f6.close()

    if(createdDate_4 != createdDate_5 or updatedDate_4 != updatedDate_5 or expiresDate_4 != expiresDate_5 or email_4 != email_5):
        flag = True

    return flag

#--------------------------------------------------------------#

def read_domain_4():
    flag = False
    # Opening JSON file for domain #4
    f7 = open(hngleg_domain,)
    # returns JSON object as dict
    data = json.load(f7)
    createdDate_6 = data['WhoisRecord']['audit']['createdDate']
    updatedDate_6 = data['WhoisRecord']['audit']['updatedDate']
    expiresDate_6 = data['WhoisRecord']['registryData']['expiresDate']
    email_6 = data['WhoisRecord']['contactEmail']
    if(not email_6):
        email_6 = "no emails registered"
    f7.close()

    f8 = open(hngleg_domain_2,)
    data1 = json.load(f8)
    createdDate_7 = data1['WhoisRecord']['audit']['createdDate']
    updatedDate_7 = data1['WhoisRecord']['audit']['updatedDate']
    expiresDate_7 = data1['WhoisRecord']['registryData']['expiresDate']
    email_7 = data1['WhoisRecord']['contactEmail']
    if(not email_7):
        email_7 = "no emails registered"
    f8.close()

    if(createdDate_6 != createdDate_7 or updatedDate_6 != updatedDate_7 or expiresDate_6 != expiresDate_7 or email_6 != email_7):
        flag = True

    return flag

#--------------------------------------------------------------#

def read_domain_5():
    flag = False
    # Opening JSON file for domain #5
    f9 = open(pionsecar_domain,)
    # returns JSON object as dict
    data = json.load(f9)
    createdDate_8 = data['WhoisRecord']['createdDate']
    updatedDate_8 = data['WhoisRecord']['updatedDate']
    expiresDate_8 = data['WhoisRecord']['expiresDate']
    email_8 = data['WhoisRecord']['contactEmail']
    if(not email_8):
        email_8 = "no emails registered"
    f9.close()

    f10 = open(pionsecar_domain_2,)
    data1 = json.load(f10)
    createdDate_9 = data1['WhoisRecord']['createdDate']
    updatedDate_9 = data1['WhoisRecord']['updatedDate']
    expiresDate_9 = data1['WhoisRecord']['expiresDate']
    email_9 = data1['WhoisRecord']['contactEmail']
    if(not email_9):
        email_9 = "no emails registered"
    f10.close()

    if(createdDate_8 != createdDate_9 or updatedDate_8 != updatedDate_9 or expiresDate_8 != expiresDate_9 or email_8 != email_9):
        flag = True

    return flag

# ------- end of reading JSON files ----------------------- #

#comparison of domain fields


if(read_domain_1()):
    subject = "Automatic alert generated for domain www.buildarat.com"
    body = "This is an email with attachment sent from Python"
    sender_email = "oscarrm980@gmail.com"
    receiver_email = "oscarrm980@gmail.com"
    password = "Pelu123!"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "{}/data_domain_www.buildarat.com_0.json".format(current_path)  # In same directory as script

    # Open file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if(read_domain_2()):
    subject = "Automatic alert generated for domain www.disorderstatus.ru"
    body = "This is an email with attachment sent from Python"
    sender_email = "oscarrm980@gmail.com"
    receiver_email = "oscarrm980@gmail.com"
    password = "Pelu123!"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "{}/data_domain_www.disorderstatus.ru_0.json".format(current_path)  # In same directory as script

    # Open file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if(read_domain_3()):
    subject = "Automatic alert generated for domain www.garatinterbk.online"
    body = "This is an email with attachment sent from Python"
    sender_email = "oscarrm980@gmail.com"
    receiver_email = "oscarrm980@gmail.com"
    password = "Pelu123!"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "{}/data_domain_www.garatinterbk.online_0.json".format(current_path)  # In same directory as script

    # Open file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if(read_domain_4()):
    subject = "Automatic alert generated for domain www.hngleg.online"
    body = "This is an email with attachment sent from Python"
    sender_email = "oscarrm980@gmail.com"
    receiver_email = "oscarrm980@gmail.com"
    password = "Pelu123!"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "{}/data_domain_www.hngleg.online_0.json".format(current_path)  # In same directory as script

    # Open file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if(read_domain_5()):
    subject = "Automatic alert generated for domain www.pionsecar.com"
    body = "This is an email with attachment sent from Python"
    sender_email = "oscarrm980@gmail.com"
    receiver_email = "oscarrm980@gmail.com"
    password = "Pelu123!"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "{}/data_domain_www.pionsecar.com_0.json".format(current_path)  # In same directory as script

    # Open file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)