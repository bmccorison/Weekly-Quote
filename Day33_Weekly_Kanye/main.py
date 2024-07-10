import smtplib
import datetime as dt
import requests
from random import choice

sender_email = ""
password = ""
receiver_gmail = ""



now = dt.datetime.now()
print(now.weekday())

if now.weekday() == 3:
    with open("Week.txt", "r") as week_file:
        weeks_lived = int(week_file.read())
        weeks_left = 3962 - weeks_lived
    with open("Week.txt", "w") as week_file:
        week_file.write(str(weeks_lived + 1))

    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    data_quote = data["quote"]
    today_quote = "'"+ data_quote + "' - Kanye 'Ye' West"

    print(today_quote)
    print(weeks_left)
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_gmail,
                            msg=f"Subject:Your Monday Motivation!\n\nYOU HAVE {weeks_left} WEEKS LEFT TO LIVE!(On Average)"
                                f"\n\nAnyway heres your quote!\n{today_quote}"
       )
