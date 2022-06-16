from django import forms
from news_article.models import NewsArticle

class NewsAricleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['uuid', 'title', 'create_date', 'update_date', 'body']