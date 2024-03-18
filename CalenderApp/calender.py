import sqlite3
import datetime
import calendar
from datetime import datetime, timedelta
def buildcalender():
    year = datetime.now().year
    month = datetime.now().month
    num_days = calendar.monthrange(year, month)[1]
    first_day = calendar.weekday(year, month, 1)
    first_day = (first_day+1)%7
    dayss = ["S","M","T","W","T","F","S"]
    # Get the number of days in the given month
    _, num_days = calendar.monthrange(year, month)
    # Calculate the number of weeks using integer division
    num_weeks = (num_days + calendar.weekday(year, month, 1)) // 7 + 1
    days = []
    weeks = []
    centered_year = str(year).center(35)
    print(centered_year)
    for day in dayss:
        print(f"{day:^5}", end='')
    print()
    for i in range(1,num_days+first_day+1):
        if i<=first_day:
            days.append("")
        else:
            days.append(i - first_day)
    for i in range(0, len(days), 7):
        print("ー"*18)
        # Slice the original list to create sublists of size 7
        sublist = days[i:i+7]
        for day in sublist:
            print(f"|{day:^4}",end='')
        # Append the sublist to the list of sublists
        print("|")
        weeks.append(sublist)
    print("ー"*3*len(weeks[5]))
def ask():
    print("Welcome to your 2024 calender!")
    buildcalender()
    print("Here are your options:\n(A) Add Event\n(E) View Events\n(N) Next Month\n(P) Previous Month\n(Y) View Year")
    option = input("")
    if option in ["V","v"]:
        buildcalender()
    else:
        print("Invalid")
def main():
    ask()
main()