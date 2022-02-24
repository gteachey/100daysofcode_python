import smtplib
import datetime as dt
import random

now = dt.datetime.now()
# birth_date = (dt.datetime(year=1981, month=5, day=19))
# print(birth_date)

if now.weekday() == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()

    smtp_provider = "smtp.gmail.com"
    my_email = "gt100daysofcode@gmail.com"
    password = "T..h7RP#tz;G[t27bC,y"
    with smtplib.SMTP(smtp_provider) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="To:gteachey@outlook.com",
            msg=f"Subject:Motivational Quote of the Week\n\n{random.choice(quotes)}"
        )
