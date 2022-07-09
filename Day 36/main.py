import smtplib
import requests
from datetime import date, timedelta

EMAIL = "mail@gmail.com"
PASSWORD = "password"
STOCK_API_KEY = "key"
NEWS_API_KEY = "key"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact",
}

response = requests.get(
    "https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]

yesterday = (date.today() - timedelta(days=1)).isoformat()
two_days_ago = (date.today() - timedelta(days=2)).isoformat()

value_two_days_ago = float(data[two_days_ago]["4. close"])
value_yeterday = float(data[yesterday]["4. close"])
difference = ((value_yeterday-value_two_days_ago)/value_yeterday) * 100


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(difference) >= 5:
    parameters = {
        "q": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(
        "https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data = response.json()
    data = data["articles"][:3]

# Used GMAIL instead
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    msg_string = ""
    if difference > 0:
        symbol = "🔺"
    elif difference < 0:
        symbol = "🔻"
    else:
        symbol = ""
    for article in data:
        msg_string += f"{STOCK}: {symbol}{round(difference)}%\nHeadline: {article['title']}\nBrief: {article['description']}\n\n"
    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()
        conn.login(EMAIL, PASSWORD)
        conn.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                      msg=f"Subject:Stock Change\n\n{msg_string}")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
