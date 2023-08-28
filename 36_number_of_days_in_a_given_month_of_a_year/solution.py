import calendar

if __name__ == '__main__':
    year = int(input('Enter the year: '))
    month = int(input('Enter the month: '))
    print(f'{calendar.monthrange(year, month)[1]} days')