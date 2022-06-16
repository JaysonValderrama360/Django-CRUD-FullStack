from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    uuid=models.CharField(max_length=100)
    title=models.CharField(max_length=500)
    create_date=models.DateTimeField()
    update_date=models.DateTimeField()
    body=models.TextField()
    
    def __str__(self):
        return self.uuid
