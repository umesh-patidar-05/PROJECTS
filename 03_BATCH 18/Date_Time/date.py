from datetime import datetime


def today():
    from datetime import datetime
    now=datetime.today()
    current = now.strftime("%d-%B-%Y")
    return current


def days_left():
     
    today = datetime.today()
    last_date = datetime(2027, 2, 2)
    days_left = (last_date - today).days
    return days_left
    