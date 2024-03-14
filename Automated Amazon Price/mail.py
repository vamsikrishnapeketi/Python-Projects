import smtplib
import config

my_email = config.my_email
password = config.password
to_email = config.to_email

class Mail():
    def __init__(self,price,product_name):
        self.product_name = product_name
        self.price = price
        self.body = f"The {self.product_name} is the cheapest now .\n The product price is {self.price}.Go order it now "

    def send_myself_mail(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() 
            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject: Amazon wish list product on discount\n\n{self.body}")
            connection.close() 