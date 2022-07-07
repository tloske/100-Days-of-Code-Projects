import smtplib
import datetime
from random import choice

my_email = "test@test.com"
password = "test"

if datetime.datetime.now().isoweekday() == 1:
    with open("quotes.txt") as file:
        quotes = file.readlines()

    quote = choice(quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr="test@test.com",
                      to_addrs="recipient@recep.com",
                      msg=f"Subject:hello\n\n{quote}")
