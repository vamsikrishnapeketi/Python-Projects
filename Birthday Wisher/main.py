import datetime as dt
import pandas
import smtplib 
import random
import config

my_email = config.my_email
password = config.password

data = pandas.read_csv("birthdays.csv")

current_time = dt.datetime.now()

date = (current_time.year, current_time.month, current_time.day)

birthday_dict = {(row.month,row.day): row for (index,row) in data.iterrows()}

if date in birthday_dict:
    birthday_person = birthday_dict[date]
    file_path = f"letter_templates/letter_{random.ranint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)    
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
            )