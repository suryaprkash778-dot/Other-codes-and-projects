print("welcome to python pizza deliveries!")
size=(input("what size pizza do you want? small,medium or large\n"))
print("prices are, small pizza:15$ , medium pizza:20$ , large pizza:25$")
bill=0
pepperoni=input("do you want pepperoni on your pizza? yes or no\n")
print(" price for pepperoni is different for each pizza! its 2$ for small size , 3$ for medium and large pizza")
print("price for extra cheese is 1$ for each size")
cheese=input("do you want extra cheese on your pizza? yes or no\n")
if size=="small":
    bill=15
    if pepperoni=="yes":
        bill+=2
elif size=="medium":
    bill=20
    if pepperoni=="yes":
        bill+=3
else:
    bill=25
    if pepperoni=="yes":
        bill+=3
if cheese=="yes":
    bill+=1
print(f"your final bill is :${bill}.")

