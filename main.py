import datetime as dt
import smtplib
import pandas
import random

my_email = "Sender email id"
password = "Generated app password"

data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read()
    new_letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{new_letter}")
    print("Mail sent successfully")
