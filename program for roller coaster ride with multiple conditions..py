height=int(input("what is your height in cm?\n"))
if height>120:
    print("you can ride the roller coaster!")
    age = int(input("how old are you?\n"))
    if age<=12:
        print("ticket price for childrens is 5$.")
        bill=5
    elif age<=18:
        print("ticket price for youth is 7$.")
        bill=7
    else:
        print("ticket price for adult is 12$.")
        bill=12
    want_photo=input("do you want a photo , while riding the roller coaster?\n")
    if want_photo == "yes":
       bill += 3
       print(f"yor total bill is :{bill}$")
else:
    print("yo can't ride the roller coaster , go back to your home.")

