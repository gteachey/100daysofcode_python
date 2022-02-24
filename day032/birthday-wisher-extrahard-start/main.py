##################### Extra Hard Starting Project ######################
import random
import smtplib
import datetime
import pandas

birthday_csv = pandas.read_csv("birthdays.csv")

today = datetime.datetime.now()
month = today.month
day = today.day

for index, row in birthday_csv.iterrows():  # iterrate through the DataFrame rows, ignore the index since we don't need it
    if month == row.month and day == row.day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}") as file:
            letter = file.read()

        to_field = row.email
        update_letter = f"to: {to_field}\nSubject:HAPPY BIRTHDAY!!!\n\n" + letter.replace("[NAME]", row['name'])
        print(update_letter)
        smtp_provider = "smtp.gmail.com"
        my_email = "gt100daysofcode@gmail.com"
        password = "T..h7RP#tz;G[t27bC,y"
        with smtplib.SMTP(smtp_provider) as smtp:
            smtp.starttls()
            smtp.login(user=my_email, password=password)
            smtp.sendmail(from_addr=my_email, to_addrs=row.email, msg=update_letter)
