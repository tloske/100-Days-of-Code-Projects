import pandas
from random import choice
import datetime as dt
import smtplib
from random import randint

my_email = "test@test.com"
password = "test"
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient='records')
# 2. Check if today matches a birthday in the birthdays.csv
date = dt.datetime.now()

for birthday in birthdays:
    month = birthday['month']
    day = birthday['day']

    if month == date.month and day == date.day:
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as file:
            template = file.read()
        template = template.replace("[NAME]", birthday['name'])
        print(template)

        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(from_addr="test@test.com",
                          to_addrs=birthday['email'],
                          msg=f"Subject:hello\n\n{template}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
