from django.db import models

# Create your models here.
class Article(models.Model):
    pub_date = models.DateTimeField("date published")
    title = models.TextField()
    content = models.TextField()