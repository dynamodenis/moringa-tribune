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

def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term=request.GET.get('article')
        searched_articles=Article.search_by_title(search_term)
        message=f'{search_term}'

        return render(request,'all-news/search.html',{'message':message,'articles':searched_articles})

    else:
        message="You haven't  searched for any term"
        return render(request,'all-news/search.html',{'message':message})

def article(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
    except DoesNotExist:
            raise Http404()
    
    return render(request,'all-news/article.html',{'article':article})