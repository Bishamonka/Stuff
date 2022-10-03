import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

# Check current week day
current_time = dt.datetime.now()
current_day_of_week = current_time.weekday()
if current_day_of_week == 0:

    # Pick new quote
    with open("quotes.txt") as data_file:
        content = data_file.read()
        quotes = content.split("\n")

    new_quote = random.choice(quotes)

    # Send New Email
    my_email = "example@hotmail.com"
    password = "password"

    msg = MIMEText(new_quote)
    msg['Subject'] = "Monday Motivating Quotes"

    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="example@mail.com", msg=msg.as_string())






