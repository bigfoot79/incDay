def dayCountPerMonth(year, month):
    # Days per month is simple for all months except February, which is dependant until the leap year.
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        # month is February and dependant until whether or not it is a leap year.
        if year % 400 == 0:
            return 29
        elif year % 100 == 0:
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28


def main():
    day = 1
    month = 8
    year = 2015
    
    while year < 2019:
        print("Date: %2d/%2d/%4d" % (day, month, year))
        monthDays = dayCountPerMonth(year, month)
        if day < monthDays:
            day = day + 1
        else:
            day = 1
            month = month + 1
            if month > 12:
                month = 1
                year = year + 1


if __name__ == '__main__':
    main()
