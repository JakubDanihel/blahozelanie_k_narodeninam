import smtplib
import random
import datetime as dt
import pandas as pd

#zistenie dna - ulozene ako tuple
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

#ulozenie mailovej adresy a hesla pre dalsie pozuzitie
MY_MAIL = "testprogramko@gmail.com"
MY_PW = "rhoe tstn gmvl rjql "

#nacitanie dat z csv
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#vzlozenie spravy ktora sa bude posielat
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple] #zistenie mena komu ma byt tento mail adresovany
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt" #nacitanie nahodnej spravy

    #otvorenie spravy a zistenie mena adresata
    with open(file_path) as letter_file:
        contens = letter_file.read()
        contens = contens.replace("[NAME]", birthday_person["name"])

    #samotne odoslanie spravy
    with smtplib.SMTP("smtp.gmail.com") as contion:
        contion.starttls()
        contion.login(MY_MAIL, MY_PW)
        contion.sendmail(from_addr=MY_MAIL, to_addrs=birthday_person["email"], msg=f"Subject : Happy Birthday\n\n{contens}")



