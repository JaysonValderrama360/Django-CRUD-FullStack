from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name = 'all_articles'),
    path('delete_article/<int:pk>', views.deleteArticle, name = 'deleteArticle'),
    path('update_article/<int:pk>', views.updateArticle, name = 'updateArticle'),
]