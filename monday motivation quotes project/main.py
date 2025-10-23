import random
import smtplib
import datetime as dt
my_email = "s42099146@gmail.com"
password = "ynoyhjlrgzjfsyux"

now = dt.datetime.now()
week_day = now.weekday()
with open("quotes.txt") as quotes:
    quote_data = quotes.readlines()

if week_day==0:
    random_quote=random.choice(quote_data)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(from_addr=my_email, to_addrs="suryaprkash778@yahoo.com", msg=f"Subject:Quote for an awesome morning\n\n"
                                                                                        f"{random_quote}")
       connection.close()
