from django.shortcuts import redirect, render
from news_article.models import NewsArticle
from news_article.forms import NewsAricleForm

# Create your views here.
def all_articles(request):
    article = NewsArticle.objects.all()
    form = NewsAricleForm()
    if request.method == 'POST':
        form = NewsAricleForm(NewsAricleForm.pst)
        if form.is_valid():
            form.save()
    return render(request,'index.html', {'article': article, 'form': form})

def deleteArticle(request, pk):
    articles = NewsArticle.objects.get(id = pk)
    articles.delete()
    return redirect('all_articles')

def updateArticle(request, pk):
    news = NewsArticle.objects.get(id = pk)
    updateForm = NewsAricleForm(instance = news)
    if request.method == 'POST':
        updateForm = NewsAricleForm(request.POST, instance=news)
        if updateForm.is_valid():
            updateForm.save()
    return render(request, 'updateArticle.html', {'news':news, 'updateform': updateForm})
