from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
def home(request, year= datetime.now().year, month=datetime.now().strftime('%B')):
    # convert month from name to number
    month_to_num = {v: k for k,v in enumerate(calendar.month_name)}
    month_number = month_to_num.get(month.capitalize())
    cal = HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    #Current time
    time = now.strftime('%I:%M:%S %p')
    
    return render(request, 'events/home.html', {"year": year, "month": month, "month_number": month_number,"cal":cal,"now": now,"time":time})
