import datetime as dt

birth_day = int(input("Enter your birthdate \n"))
birth_month = int(input("Enter your birthmonth \n"))
birth_year = int(input("Enter your birthyear \n"))

today = dt.date.today()
print("Today is " + str(today))

birthday = dt.date(birth_year, birth_month, birth_day)
print("Your birthday is on " + str(birthday))

days_since_birth = (today - birthday).days
print("You have lived " + str(days_since_birth) + " days")


days_since_birth_in_years = int((days_since_birth / 365))
print("Your age is " + str(days_since_birth_in_years))
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# weekday = weekdays[today.weekday()]
# print('Today is a '+ str(weekday))
