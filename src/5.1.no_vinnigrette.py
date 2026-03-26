from datetime import date , timedelta
import random

#Read input dates from the user
date1_str = input("Enter the first date (YYYY-MM-DD) : ")
date2_str = input("Enter the second date (YYYY-MM-DD) : ")
 
#Convert the input strings to date objects
date1 = date.fromisoformat(date1_str)
date2 = date.fromisoformat(date2_str)

#EPOCH reference date (January 1, 1970)
epoch = date(1970, 1, 1)

#Calculate the number of days since the epoch for both dates
timestamp1 = (date1 - epoch).days
timestamp2 = (date2 - epoch).days

#Generate a random timestamp between the two timestamps
timestamp_aleatoire = random.randint(
    min(timestamp1, timestamp2),
    max(timestamp1, timestamp2)
)
date_aleatoire = epoch + timedelta(days=timestamp_aleatoire)

print(f"Date  : {date_aleatoire}")

if date_aleatoire.weekday() == 0:
    print("Ain't gettin' no vinaigrette today :(")