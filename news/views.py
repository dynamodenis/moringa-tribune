from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_of_day(request):
    date=dt.date.today()
    # day=convert_dates(date)
    # html=f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    return render(request,'all-news/today_news.html',{'date':date})

def convert_dates(dates):
    #FUNCTION THAT RETUNS THE DAY O THE WEEKEND
    day_week=dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day=days[day_week]
    return day


def past_days_news(request,past_date):
        # Converts data from the string Url
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date== dt.datetime.today():
        return redirect(news_of_day)
    # day = convert_dates(date)
    # html = f'''
    #     <html>
    #         <body>
    #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #         </body>
    #     </html>
    #         '''
    return render(request,'all-news/past_news.html',{'date':date})
