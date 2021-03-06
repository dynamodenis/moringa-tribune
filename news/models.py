from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20,blank=True)

    def save_editor(self):
        self.save()
    @classmethod
    def delete_editor(cls,name):
        Editor.objects.get(first_name=name).delete()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering=['first_name']

class Tags(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=60)
    post=models.TextField()
    editor=models.ForeignKey(Editor)
    tags=models.ManyToManyField(Tags)
    pub_date=models.DateTimeField(auto_now_add=True)
    article_image=models.ImageField(upload_to='articles/',blank=True)

    @classmethod
    def get_today(cls):
        today=dt.date.today()
        news=cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls,date):
        news=cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news=cls.objects.filter(title__icontains=search_term)
        return news
