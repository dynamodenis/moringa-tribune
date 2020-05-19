from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_of_day(request):
    date=dt.date.today()
    news=Article.get_today()
    return render(request,'all-news/today_news.html',{'date':date,'news':news})

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
    news=Article.days_news(date)
    return render(request,'all-news/past_news.html',{'date':date,'news':news})
