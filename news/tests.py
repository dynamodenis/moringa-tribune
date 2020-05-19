from django.test import TestCase
from .models import Editor,Tags,Article
import datetime as dt
# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

#TEST SAVE OBJECTS
    def test_save_editor(self):
        self.james.save_editor()
        editor=Editor.objects.all()
        self.assertTrue(len(editor)>0)

#TEST DELETE OBJECTS
    def test_delete_object(self):
        self.james.save_editor()
        delete=Editor.delete_editor('James')
        self.assertTrue(len(Editor.objects.all())==0)

class ArticleTestClass(TestCase):
    #Creating A new editor and saving it
    # Creating a new editor and saving it
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_today_news(self):
        
        get=Article.get_today()
        self.assertTrue(len(get)>0)

    def test_get_news_by_date(self):
        test_date='2017-03-17'
        date=dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)


