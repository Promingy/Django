from django.db import models

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    active    = models.BooleanField(default=False)


